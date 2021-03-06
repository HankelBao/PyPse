from lark import Tree
from copy import deepcopy
from .debug import Debug, DebugOutput
from .output import register_current_block
from .symbols import Symbol, Symbols
from .values import ValueType, Value
from .expressions import Expression
from .keys import Key
from .converters import token_find_data, convert_param_tokens_to_param_items, convert_symbol_token_to_symbol_name, convert_token_to_valuetype, get_array_info_from_token, get_custom_type_name_from_type_token, token_find_multiple_data


class Block():
    def __init__(self, parentblock):
        self.childblocks = []
        self.symbols = Symbols()
        self.parentblock = parentblock

    def run(self, block_token: Tree):
        pass

    def recursive_debug_output(self):
        DebugOutput.output_block_title("anonymous block")

    def run_childblocks(self, blocks_token):
        self.childblocks = []
        for block_token in blocks_token.children:
            if block_token.data in blocks:
                MatchedBlock = blocks[block_token.data]
            else:
                MatchedBlock = Block
            block = MatchedBlock(self)
            register_current_block(block, block_token)
            block.run(block_token)
            self.childblocks.append(block)

    def search_symbol_by_name_recursively(self, symbol_name):
        block = self
        symbol = None
        while not symbol:
            if not block:
                return None
            symbol = block.symbols.search_by_name(symbol_name)
            block = block.parentblock
        return symbol

    def recursive_debug_output_childblocks(self):
        self.recursive_debug_output_childblocks_with_attr(
            self.childblocks, "childblocks")

    def recursive_debug_output_childblocks_with_attr(self, childblocks, attr: str):
        DebugOutput.output_block_attr(attr)
        DebugOutput.increase_depth()
        for block in childblocks:
            block.recursive_debug_output()
        DebugOutput.decrease_depth()

    def __repr__(self):
        return type(self).__name__


class DebugBlock(Block):
    def run(self, block_token: Tree):
        Debug.get_root_block().recursive_debug_output()

    def recursive_debug_output(self):
        pass


class RootBlock(Block):
    def run(self, block_token: Tree):
        self.run_childblocks(block_token)

    def init_sys_symbols(self):
        symbol_true = Symbol("TRUE", ValueType.BOOL)
        symbol_true.value.assign_value_in_python(True)
        symbol_false = Symbol("FALSE", ValueType.BOOL)
        symbol_false.value.assign_value_in_python(False)
        self.symbols.append(symbol_true)
        self.symbols.append(symbol_false)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("root block")
        DebugOutput.increase_depth()
        self.symbols.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class DeclareBlock(Block):
    def run(self, block_token: Tree):
        # Name
        variable_name_token = token_find_data(block_token, "symbol")
        variable_name = convert_symbol_token_to_symbol_name(
            variable_name_token)

        # Type
        valuetype_token = token_find_data(block_token, "type")
        valuetype = convert_token_to_valuetype(valuetype_token)
        if valuetype == ValueType.CUSTOM_TYPE:
            valuetype_name = get_custom_type_name_from_type_token(
                valuetype_token)
            valuetype_symbol = self.search_symbol_by_name_recursively(
                valuetype_name)
            valuetype = deepcopy(valuetype_symbol.value.value_in_python)

        self.symbol = Symbol(variable_name, valuetype)

        # Initiation
        if valuetype == ValueType.ARRAY:
            start_index, end_index, valuetype = get_array_info_from_token(
                valuetype_token)
            self.symbol.value.value_in_python = {}
            for i in range(start_index, end_index+1):
                self.symbol.value.value_in_python[i] = Value(valuetype)
        if isinstance(valuetype, TypeBlock):
            self.symbol.value.value_in_python = deepcopy(valuetype)

        # Merge
        self.parentblock.symbols.append(self.symbol)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("declare block")
        DebugOutput.increase_depth()
        DebugOutput.output_block_attr("defined symbol")
        DebugOutput.increase_depth()
        self.symbol.debug_output()
        DebugOutput.decrease_depth()
        DebugOutput.decrease_depth()


class AssignBlock(Block):
    def run(self, block_token: Tree):
        key_token = None
        expression_token = None
        for token in block_token.children:
            if token.data == "key":
                key_token = token
            if token.data == "expression":
                expression_token = token
        self.key = Key(key_token, self)
        self.expression = Expression(expression_token, self)
        self.key.set_value(self.expression.get_value())

    def recursive_debug_output(self):
        DebugOutput.output_block_title("assign block")
        DebugOutput.increase_depth()

        self.key.debug_output()
        self.expression.debug_output()

        DebugOutput.decrease_depth()


class TypeBlock(Block):
    def run(self, block_token: Tree):
        symbol_token = token_find_data(block_token, "symbol")
        childblocks = token_find_data(block_token, "blocks")
        self.symbol_name = convert_symbol_token_to_symbol_name(symbol_token)

        symbol = Symbol(self.symbol_name, ValueType.TYPE)
        symbol.value.assign_value_in_python(self)
        self.parentblock.symbols.append(symbol)

        self.run_childblocks(childblocks)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("type block")
        DebugOutput.increase_depth()

        DebugOutput.output_block_attr("symbol_name")
        DebugOutput.increase_depth()
        DebugOutput.output(self.symbol_name)
        DebugOutput.decrease_depth()

        self.recursive_debug_output_childblocks()

        DebugOutput.decrease_depth()


class OutputBlock(Block):
    def run(self, block_token: Tree):
        expression_token = None
        for token in block_token.children:
            if token.data == "expression":
                expression_token = token
        self.expression = Expression(expression_token, self)
        print(str(self.expression.get_value().value_in_python))

    def recursive_debug_output(self):
        DebugOutput.output_block_title("output block")
        DebugOutput.increase_depth()

        self.expression.debug_output()

        DebugOutput.decrease_depth()


class InputBlock(Block):
    def run(self, block_token: Tree):
        key_token = token_find_data(block_token, "key")
        self.key = Key(key_token, self)
        input_value_in_python = int(input())
        self.key.set_value_in_python(input_value_in_python)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("input block")
        DebugOutput.increase_depth()

        self.key.debug_output()

        DebugOutput.decrease_depth()


class DecisionBlock(Block):
    def run(self, block_token: Tree):
        decision_if_branch_token = token_find_data(
            block_token, "decision_if_branch")
        decision_condition_expression_token = token_find_data(
            decision_if_branch_token, "expression")
        self.decision_condition_expression = Expression(
            decision_condition_expression_token, self)
        decision_if_blocks_token = token_find_data(
            decision_if_branch_token, "blocks")

        self.decision_else_branch_exist = False
        decision_else_branch_token = token_find_data(
            block_token, "decision_else_branch")
        if decision_else_branch_token:
            self.decision_else_branch_exist = True
            decision_else_blocks_token = token_find_data(
                decision_else_branch_token, "blocks")

        if self.decision_condition_expression.get_value().value_in_python == True:
            self.run_childblocks(decision_if_blocks_token)
        else:
            if self.decision_else_branch_exist == True:
                self.run_childblocks(decision_else_blocks_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("decision block")
        DebugOutput.increase_depth()

        self.decision_condition_expression.debug_output()
        DebugOutput.output_block_attr("executed branch")
        DebugOutput.increase_depth()
        for block in self.childblocks:
            block.recursive_debug_output()
        DebugOutput.decrease_depth()

        DebugOutput.decrease_depth()


class CaseBlock(Block):
    def run(self, block_token: Tree):
        case_key_token = token_find_data(block_token, "key")
        case_key = Key(case_key_token, self)
        case_key_value = case_key.get_value().value_in_python
        cases = {}
        case_otherwise = None
        for child_token in token_find_multiple_data(block_token, "case"):
            case_exp_token = token_find_data(child_token, "expression")
            if case_exp_token:
                case_exp = Expression(case_exp_token, self)
                if case_exp.get_value().value_in_python == case_key_value:
                    blocks_token = token_find_data(child_token, "blocks")
                    self.run_childblocks(blocks_token)
                    return
            else:
                case_otherwise = token_find_data(child_token, "blocks")
        if case_otherwise:
            self.run_childblocks(case_otherwise)


class RepeatBlock(Block):
    def run(self, block_token: Tree):
        blocks_token = token_find_data(block_token, "blocks")
        condition_exp_token = token_find_data(block_token, "expression")
        self.condition_exp = Expression(condition_exp_token, self)
        self.run_childblocks(blocks_token)
        while self.condition_exp.get_value().value_in_python == False:
            self.run_childblocks(blocks_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("repeat block")
        DebugOutput.increase_depth()
        self.condition_exp.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class WhileBlock(Block):
    def run(self, block_token: Tree):
        blocks_token = token_find_data(block_token, "blocks")
        condition_exp_token = token_find_data(block_token, "expression")
        self.condition_exp = Expression(condition_exp_token, self)
        while self.condition_exp.get_value().value_in_python == True:
            self.run_childblocks(blocks_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("while block")
        DebugOutput.increase_depth()
        self.condition_exp.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class ForBlock(Block):
    def run(self, block_token: Tree):
        key_token = token_find_data(block_token, "key")
        self.key = Key(key_token, self)
        for_start_exp_token = token_find_data(block_token, "for_start_exp")
        self.for_start_exp = Expression(for_start_exp_token, self)
        for_end_exp_token = token_find_data(block_token, "for_end_exp")
        self.for_end_exp = Expression(for_end_exp_token, self)
        blocks_token = token_find_data(block_token, "blocks")

        self.key.set_value(self.for_start_exp.get_value())
        while self.key.get_value().value_in_python <= self.for_end_exp.get_value().value_in_python:
            self.run_childblocks(blocks_token)
            value = self.key.get_value()
            value.value_in_python += 1
            self.key.set_value(value)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("for block")
        DebugOutput.increase_depth()
        self.key.debug_output()
        self.for_start_exp.debug_output()
        self.for_end_exp.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class FunctionBlock(Block):
    def run(self, block_token: Tree):
        function_name_token = token_find_data(block_token, "symbol")
        param_tokens = token_find_data(block_token, "function_block_params")
        function_return_type_token = token_find_data(block_token, "type")

        self.function_name = convert_symbol_token_to_symbol_name(
            function_name_token)
        function_return_type = \
            convert_token_to_valuetype(function_return_type_token)

        self.param_symbols = []
        param_items = convert_param_tokens_to_param_items(param_tokens)
        for param_item in param_items:
            symbol_name = param_item['param_name']
            value_type = param_item['param_type']
            symbol = Symbol(symbol_name, value_type)
            self.param_symbols.append(symbol)
            self.symbols.append(symbol)

        self.return_value = Value(function_return_type)
        self.blocks_token = token_find_data(block_token, "blocks")

        function_symbol = Symbol(self.function_name, ValueType.FUNCTION)
        function_symbol.value.assign_value_in_python(self)
        self.parentblock.symbols.append(function_symbol)

    def call(self, param_exps):
        if len(param_exps) != len(self.param_symbols):
            return
        for index, param_exp in enumerate(param_exps):
            symbol_name = self.param_symbols[index].name
            symbol = self.symbols.search_by_name(symbol_name)
            symbol.value.assign_value(param_exp.get_value())
        self.run_childblocks(self.blocks_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("function block")
        DebugOutput.increase_depth()
        DebugOutput.output_block_attr("name")
        DebugOutput.output(self.function_name)

        DebugOutput.output_block_attr("params")
        DebugOutput.output(self.param_symbols)

        DebugOutput.output_block_attr("return")
        self.return_value.debug_output()
        DebugOutput.decrease_depth()


class ReturnBlock(Block):
    def run(self, block_token: Tree):
        return_exp_token = token_find_data(block_token, "expression")
        self.return_exp = Expression(return_exp_token, self)

        def recursive_search_parent_function_block(current_block):
            block = current_block
            while not isinstance(block, FunctionBlock):
                if not block:
                    return None
                block = block.parentblock
            return block
        parent_function_block = recursive_search_parent_function_block(self)
        parent_function_block.return_value.assign_value(
            self.return_exp.get_value())

    def recursive_debug_output(self):
        DebugOutput.output_block_title("return block")
        DebugOutput.increase_depth()
        self.return_exp.debug_output()
        DebugOutput.decrease_depth()


class ProcedureBlock(Block):
    def run(self, block_token: Tree):
        procedure_name_token = token_find_data(block_token, "symbol")
        procedure_name = convert_symbol_token_to_symbol_name(
            procedure_name_token)
        param_tokens = token_find_data(block_token, "function_block_params")

        self.param_symbols = []
        param_items = convert_param_tokens_to_param_items(param_tokens)
        for param_item in param_items:
            symbol_name = param_item['param_name']
            value_type = param_item['param_type']
            symbol = Symbol(symbol_name, value_type)
            self.param_symbols.append(symbol)
            self.symbols.append(symbol)

        self.blocks_token = token_find_data(block_token, "blocks")

        procedure_symbol = Symbol(procedure_name, ValueType.PROCEDURE)
        procedure_symbol.value.assign_value_in_python(self)
        self.parentblock.symbols.append(procedure_symbol)

    def call(self, param_exps):
        if len(param_exps) != len(self.param_symbols):
            return
        for index, param_exp in enumerate(param_exps):
            symbol_name = self.param_symbols[index].name
            symbol = self.symbols.search_by_name(symbol_name)
            symbol.value.assign_value(param_exp.get_value())
        self.run_childblocks(self.blocks_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("procedure block")
        DebugOutput.increase_depth()
        self.symbols.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class CallProcedureBlock(Block):
    def run(self, block_token: Tree):
        procedure_name_token = token_find_data(block_token, "key")

        function_params_token = token_find_data(block_token, "function_params")
        param_exps = []
        for expression_token in function_params_token.children:
            if expression_token.data == "expression":
                param_exp = Expression(expression_token, self)
                param_exps.append(param_exp)

        self.procedure_key = Key(procedure_name_token, self)
        procedure = self.procedure_key.get_value()
        procedure_block = procedure.value_in_python
        procedure_block.call(param_exps)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("call block")
        DebugOutput.increase_depth()
        self.procedure_key.debug_output()
        DebugOutput.decrease_depth()


blocks = {
    "debug_block": DebugBlock,
    "declare_block": DeclareBlock,
    "type_block": TypeBlock,
    "assign_block": AssignBlock,
    "output_block": OutputBlock,
    "input_block": InputBlock,
    "decision_block": DecisionBlock,
    "repeat_block": RepeatBlock,
    "while_block": WhileBlock,
    "for_block": ForBlock,
    "procedure_block": ProcedureBlock,
    "call_procedure_block": CallProcedureBlock,
    "function_block": FunctionBlock,
    "return_block": ReturnBlock,
    "case_block": CaseBlock,
}

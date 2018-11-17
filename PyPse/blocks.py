from lark import Tree
from .debug import Debug, DebugOutput
from .symbols import Symbol, Symbols, convert_token_to_symbol_name
from .values import convert_token_to_valuetype, ValueType, Value
from .expressions import Expression
from .keys import Key
from .converters import token_find_data, convert_param_tokens_to_symbols


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
        childblocks = []
        for block_token in blocks_token.children:
            if block_token.data in blocks:
                MatchedBlock = blocks[block_token.data]
            else:
                MatchedBlock = Block
            block = MatchedBlock(self)
            block.run(block_token)
            # self.childblocks.append(block)
            childblocks.append(block)
        self.childblocks = childblocks

    def recursive_debug_output_childblocks(self):
        self.recursive_debug_output_childblocks_with_attr(self.childblocks, "childblocks")

    def recursive_debug_output_childblocks_with_attr(self, childblocks, attr: str):
        DebugOutput.output_block_attr(attr)
        DebugOutput.increase_depth()
        for block in childblocks:
            block.recursive_debug_output()
        DebugOutput.decrease_depth()


class DebugBlock(Block):
    def run(self, block_token: Tree):
        Debug.get_root_block().recursive_debug_output()

    def recursive_debug_output(self):
        pass


class RootBlock(Block):
    def run(self, block_token: Tree):
        self.run_childblocks(block_token)

    def recursive_debug_output(self):
        DebugOutput.output_block_title("root block")
        DebugOutput.increase_depth()
        self.symbols.debug_output()
        self.recursive_debug_output_childblocks()
        DebugOutput.decrease_depth()


class DeclareBlock(Block):
    def run(self, block_token: Tree):
        variable_name_token = token_find_data(block_token, "symbol")
        variable_name = convert_token_to_symbol_name(variable_name_token)
        value_type = convert_token_to_valuetype(token_find_data(block_token, "type"))
        self.symbol = Symbol(variable_name, value_type)
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

        function_name = convert_token_to_symbol_name(function_name_token)
        function_return_type = \
            convert_token_to_valuetype(function_return_type_token)

        self.param_symbols = convert_param_tokens_to_symbols(param_tokens)
        for symbol in self.param_symbols:
            self.symbols.append(symbol)

        self.return_value = Value(function_return_type)
        self.blocks_token = token_find_data(block_token, "blocks")

        function_symbol = Symbol(function_name, ValueType.FUNCTION)
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


class ReturnBlock(Block):
    def run(self, block_token: Tree):
        return_exp_token = token_find_data(block_token, "expression")
        self.return_exp = Expression(return_exp_token, self)
        # Error may appear here when the parent block is not a function
        # TODO: Fixme
        self.parentblock.return_value.assign_value(self.return_exp.get_value())

    def recursive_debug_output(self):
        DebugOutput.output_block_title("return block")
        DebugOutput.increase_depth()
        self.return_exp.debug_output()
        DebugOutput.decrease_depth()


class ProcedureBlock(Block):
    def run(self, block_token: Tree):
        procedure_name_token = token_find_data(block_token, "symbol")
        procedure_name = convert_token_to_symbol_name(procedure_name_token)
        param_tokens = token_find_data(block_token, "function_block_params")
        self.param_symbols = convert_param_tokens_to_symbols(param_tokens)
        for symbol in self.param_symbols:
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

        procedure_key = Key(procedure_name_token, self)
        procedure = procedure_key.get_value()
        procedure_block = procedure.value_in_python
        procedure_block.call(param_exps)


blocks = {
    "debug_block": DebugBlock,
    "declare_block": DeclareBlock,
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
}

from .block import Block, register_block
from .precompiler import CodeLine
from .symbols import Symbol, SymbolType, create_symbol_variable
from .values import Value, ValueType, get_ValueType_by_name
from .operations import OperationTypeAssign, OperationTypeLargerThan, OperationTypeSmallerThan, OperationTypeAddByOne
from .keys import Key
from .expressions import Expression


class ProgramBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        return False, True

    def compile(self, code_lines: list):
        children_blocks = self.compile_rest(code_lines)
        self.data['children_blocks'] = children_blocks

    def run(self):
        for child_block in self.data['children_blocks']:
            child_block.run()

"""
DECLARE Variable_Name : Variable_Type[Subs] OF ...
"""
class DeclareBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.get_word_by_index(0) == "DECLARE":
            return True, True
        else:
            return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        symbol_name_str = code_line.str_between("DECLARE", ":").strip(" ")
        value_type_str = code_line.content[code_line.content.index(":")+1:].strip(" ")
        symbol = create_symbol_variable(symbol_name_str, value_type_str)
        self.parent.symbols.add(symbol)

    def run(self):
        pass


"""
Variable_Key <- Expression
"""
class AssignBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include(OperationTypeAssign.identifier):
            return True, True
        return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        left_exp, right_exp = code_line.split(OperationTypeAssign.identifier)
        self.data['key'] = Key(left_exp, self.parent)
        self.data['expression'] = Expression(right_exp, self.parent)

    def run(self):
        symbol = self.data['key'].get_symbol()
        value = self.data['expression'].get_value()
        symbol.symbol_value.assign_value(value)


class OutputBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("OUTPUT"):
            return True, True
        return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        _, exp = code_line.split("OUTPUT")
        self.data['expression'] = Expression(exp, self.parent)

    def run(self):
        value = self.data['expression'].get_value()
        print(str(value.value_in_python))


class InputBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("INPUT"):
            return True, True
        return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        _, exp = code_line.split("INPUT")
        self.data['key'] = Key(exp, self.parent)

    def run(self):
        value_in_python = input()
        key = self.data['key']
        key.get_symbol().symbol_value.assign_value_in_python(value_in_python)


"""
IF ExpressionInBoolType
  THEN
    BLOCKS
ELSE
    BLOCKS
ENDIF
"""
class BranchesBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("ENDIF"):
            return True, True
        if code_line.if_include("IF"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        class Branch():
            def __init__(self, condition_exp: Expression, branch_blocks: Block):
                self.condition_exp = condition_exp
                self.branch_blocks = branch_blocks

            def check_condition(self):
                if self.condition_exp.get_value().value_in_python is True:
                    return True
                return False

            def __repr__(self):
                return f"Branch Condition: {self.condition_exp}"

        def add_branch(branch_condition_exp, branch_code_lines: list):
            branch_blocks = self.compile_rest(branch_code_lines)
            branch = Branch(branch_condition_exp, branch_blocks)
            self.data['branches'].append(branch)

        def create_if_branch_condition_exp_by_code_line(code_line: CodeLine) -> Expression:
            _, branch_condition_exp_str = code_line.split("IF")
            branch_condition_exp = Expression(branch_condition_exp_str, self.parent)

            return branch_condition_exp

        # Depreciated because according to the doc
        # ElseIf branch doesn't exist at all.
        def create_else_if_branch_condition_exp_by_code_line(code_line: CodeLine) -> Expression:
            _, branch_condition_exp_str = code_line.split("ELSE IF")
            branch_condition_exp = Expression(branch_condition_exp_str, self.parent)
            return branch_condition_exp

        def create_else_branch_condition_exp() -> Expression:
            branch_condition_exp = Expression("1=1", None)
            return branch_condition_exp

        self.data['branches'] = []

        # "IF"
        branch_code_lines = []
        branch_condition_exp = create_if_branch_condition_exp_by_code_line(code_lines[0])

        for index, code_line in enumerate(code_lines):
            if index == 0 or index == 1:
                continue
            if code_line.if_include("ELSE"):
                add_branch(branch_condition_exp, branch_code_lines)
                branch_code_lines = []
                branch_condition_exp = create_else_branch_condition_exp()
                continue
            if code_line.if_include("ENDIF"):
                break
            branch_code_lines.append(code_line)

        add_branch(branch_condition_exp, branch_code_lines)

    def run(self):
        for branch in self.data['branches']:
            if branch.check_condition() is True:
                for block in branch.branch_blocks:
                    block.run()


"""
FOR *Variable_Key* <- *StartIndex* TO *EndIndex*
    *Blocks*
ENDFOR
"""
class ForBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("ENDFOR"):
            return True, True
        if code_line.if_include("FOR"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        condition_line = code_lines[0]
        _, rest_condition = condition_line.split("FOR")
        loop_variable_name, rest_condition = rest_condition.split(OperationTypeAssign.identifier)
        start_exp_str, end_exp_str = rest_condition.split("TO")
        loop_code_lines = code_lines[1: -1]

        self.loop_variable_symbol = Key(loop_variable_name, self.parent).get_symbol()
        self.start_exp = Expression(start_exp_str, self.parent)
        self.end_exp = Expression(end_exp_str, self.parent)
        self.loop_blocks = self.compile_rest(loop_code_lines)

    def run(self):
        loop_variable_symbol = self.loop_variable_symbol
        start_exp_value = self.start_exp.get_value()
        end_exp_value = self.end_exp.get_value()
        loop_value = loop_variable_symbol.symbol_value
        loop_value.assign_value(start_exp_value)
        while OperationTypeSmallerThan.operate(loop_value, end_exp_value).value_in_python:
            for block in self.loop_blocks:
                block.run()
            OperationTypeAddByOne.operate(loop_value)


"""
While *ExpressionOfBoolType* DO
    *Blocks*
ENDWHILE
"""
class WhileBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("ENDWHILE"):
            return True, True
        if code_line.if_include("WHILE"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        condition_line = code_lines[0]
        print(condition_line)
        condition_exp_str = condition_line.str_between("WHILE", "DO")
        print(condition_exp_str)
        self.condition_exp = Expression(condition_exp_str, self.parent)
        self.loop_blocks = self.compile_rest(code_lines[1:-1])

    def run(self):
        while self.condition_exp.get_value().value_in_python is True:
            for block in self.loop_blocks:
                block.run()


"""
REPEAT
    *Blocks*
UNTIL *ExpressionOfBoolType*
"""
class RepeatUntilBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("UNTIL"):
            return True, True
        if code_line.if_include("REPEAT"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        condition_line = code_lines[len(code_lines)-1]
        _, condition_exp_str = condition_line.split("UNTIL")
        self.finish_condition_exp = Expression(condition_exp_str, self.parent)
        self.loop_blocks = self.compile_rest(code_lines[1:-1])

    def run(self):
        def run_loop_once():
            for block in self.loop_blocks:
                block.run()
        while True:
            run_loop_once()
            if self.finish_condition_exp.get_value().value_in_python is True:
                break


"""
CASE OF *Variable*
    *Expression*:
        *Blocks*
    OTHERWISE
        *Blocks*
ENDCASE
"""
class CaseBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("ENDCASE"):
            return True, True
        if code_line.if_include("CASE OF"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        class Case():
            def __init__(self, case_exp: Expression, case_blocks: list):
                self.case_exp = case_exp
                self.case_blocks = case_blocks

            def check_and_run(self, case_target_exp: Expression) -> bool:
                if not self.case_exp:
                    for block in self.case_blocks:
                        block.run()
                    return True
                if self.case_exp.get_value().value_in_python == case_target_exp.get_value().value_in_python:
                    for block in self.case_blocks:
                        block.run()
                    return True
                return False

        case_target_exp_line = code_lines[0]
        _, case_target_exp_str = case_target_exp_line.split("CASE OF")
        case_target_exp = Expression(case_target_exp_str, self.parent)

        cases = []
        case_code_lines = []
        current_case_exp = None

        def add_case():
            if len(case_code_lines) > 0:
                case_blocks = self.compile_rest(case_code_lines)
                case = Case(current_case_exp, case_blocks)
                cases.append(case)
                return True
            return False

        for code_line in code_lines[1: -1]:
            code_line_content = code_line.content
            if code_line_content[-1] == ":":
                if add_case():
                    case_code_lines = []
                current_case_exp_str = code_line_content[:-1]
                current_case_exp = Expression(current_case_exp_str, self.parent)
                continue
            if code_line.if_include("OTHERWISE"):
                if add_case():
                    case_code_lines = []
                current_case_exp = None
                continue
            case_code_lines.append(code_line)
        if add_case():
            case_code_lines = []

        self.cases = cases
        self.case_target_exp = case_target_exp

    def run(self):
        for case in self.cases:
            if case.check_and_run(self.case_target_exp):
                break


class DefineFunctionBlock(Block):
    """
    FUNCTION *FunctionName*(*Param1Name : *Param1TypeName)
        *Block*
    ENDFUNCTION
    """
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("ENDFUNCTION"):
            return True, True
        if code_line.if_include("FUNCTION"):
            return True, False
        return False, True

    def compile(self, code_lines: list):
        first_line = code_lines[0]
        function_name = first_line.str_between("FUNCTION", "(").strip(" ")
        params_str = first_line.str_between("(", ")")
        function_code_lines = code_lines[1: -1]
        self.blocks = self.compile_rest(function_code_lines)

        self.param_symbols = []
        params_strs = params_str.split(",")
        for param_str in params_strs:
            variable_name, value_type_str = param_str.split(":")
            variable_name = variable_name.strip(" ")
            symbol = create_symbol_variable(variable_name, value_type_str)
            self.symbols.add(symbol)
            self.param_symbols.append(symbol)
        symbol = Symbol(function_name, SymbolType.FUNCTION)
        symbol.init_value(ValueType.FUNCTION_DEFINITION)
        symbol.symbol_value.assign_value_in_python(self)
        self.parent.symbols.add(symbol)

        return_type_str = first_line.str_after("RETURNS")
        return_type = get_ValueType_by_name(return_type_str)
        self.return_value = Value(return_type)

    def run(self):
        pass

    def call(self, param_values):
        for index, param_symbol in enumerate(self.param_symbols):
            param_symbol.symbol_value.assign_value(param_values[index])
        for block in self.blocks:
            block.run()
        return self.return_value


class ReturnBlock(Block):
    """
    RETURN *Expression*
    """
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.if_include("RETURN"):
            return True, True
        return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        _, return_exp_str = code_line.split("RETURN")
        self.return_exp = Expression(return_exp_str, self.parent)

    def run(self):
        return_value = self.return_exp.get_value()
        self.parent.return_value.assign_value(return_value)


class EmptyLineBlock(Block):
    """

    """
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.content == "":
            return True, True
        return False, True


"""
*Variable* = *Expression*
"""
class UnknownBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        return True, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        print(f"{code_line.line_num}: {code_line.content}, Unknown block")

    def run(self):
        pass


register_block(DeclareBlock)
register_block(ForBlock)
register_block(AssignBlock)
register_block(OutputBlock)
register_block(InputBlock)
register_block(BranchesBlock)
register_block(WhileBlock)
register_block(RepeatUntilBlock)
register_block(CaseBlock)
register_block(DefineFunctionBlock)
register_block(ReturnBlock)
register_block(EmptyLineBlock)
register_block(UnknownBlock)

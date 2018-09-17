from .block import Block, register_block
from .precompiler import CodeLine
from .symbols import Symbol, SymbolType
from .values import ValueType
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


class DeclareBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.get_word_by_index(0) == "DECLARE":
            return True, True
        else:
            return False, True

    def compile(self, code_lines: list):
        def get_ValueType_by_name(valuetype_str: str) -> ValueType:
            valuetype_str = valuetype_str.strip()
            if valuetype_str == "REAL":
                return ValueType.REAL
            if valuetype_str == "STRING":
                return ValueType.STRING
            if valuetype_str == "INT":
                return ValueType.INT
            if "ARRAY" in valuetype_str:
                return ValueType.ARRAY

        code_line = code_lines[0]
        symbol_name_str = code_line.get_word_by_index(1)
        value_type_str = code_line.get_word_by_index(3)
        symbol_type = SymbolType.VARIABLE
        value_type = get_ValueType_by_name(value_type_str)
        if value_type == ValueType.ARRAY:
            array_range_exp = code_line.str_between('[', ']')
            range_left_exp_str, range_right_exp_str = array_range_exp.split("..")
            array_range_left_value = Expression(range_left_exp_str, self.parent).get_value()
            array_range_right_value = Expression(range_right_exp_str, self.parent).get_value()

        symbol = Symbol(symbol_name_str, symbol_type)

        symbol.init_value(value_type)
        if value_type == ValueType.ARRAY:
            symbol.symbol_value.init_array(ValueType.INT, array_range_left_value.value_in_python, array_range_right_value.value_in_python)

        self.parent.symbols.add(symbol)

    def run(self):
        pass


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
                if self.condition_exp.get_value().value_in_python == True:
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
            if code_line.if_include("ELSE IF"):
                add_branch(branch_condition_exp, branch_code_lines)
                branch_code_lines = []
                branch_condition_exp = create_else_if_branch_condition_exp_by_code_line(code_line)
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
            if branch.check_condition() == True:
                for block in branch.branch_blocks:
                    block.run()


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
        _, condition_exp_str = condition_line.split("WHILE")
        self.condition_exp = Expression(condition_exp_str, self.parent)
        self.loop_blocks = self.compile_rest(code_lines[1:-1])

    def run(self):
        while self.condition_exp.get_value().value_in_python == True:
            for block in self.loop_blocks:
                block.run()


class EmptyLineBlock(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.content == "":
            return True, True
        return False, True


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
register_block(EmptyLineBlock)
register_block(UnknownBlock)

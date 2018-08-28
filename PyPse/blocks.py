from .block import Block
from .precompiler import CodeLine


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


class DeclareBook(Block):
    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        if code_line.getWordByIndex(0) == 'DECLARE':
            return True, True
        else:
            return False, True

    def compile(self, code_lines: list):
        code_line = code_lines[0]
        symbol_name = code_line.getWordByIndex(1)
        symbol_type = code_lines.getWordByIndex(3)
        

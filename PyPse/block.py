from .symbols import Symbols
from .precompiler import CodeLine

Blocks = []

def register_block(block):
    global Blocks
    Blocks.append(block)

class Block(object):
    """Functions that blocks may implement"""

    @staticmethod
    def match(code_line: CodeLine) -> (bool, bool):
        # matched, finished
        return False, True

    def compile(self, code_lines: list):
        pass

    def run(self):
        pass

    def call(self, param_values):
        """
        Only useful in case of functions or procedures
        """
        pass

    """Function that blocks shouldn't implement"""

    def __init__(self, parent):
        self.symbols = Symbols()
        self.data = {}
        self.parent = parent

    def compile_rest(self, code_lines: list) -> list:
        child_blocks = []

        block_lines = []
        current_Block = None

        matched, finished = False, False
        repeat_block_count = 0

        for code_line in code_lines:
            block_lines.append(code_line)

            if current_Block:
                matched, finished = current_Block.match(code_line)
                if not matched:
                    finished = False
                if matched and not finished:
                    repeat_block_count += 1
                if matched and finished:
                    if repeat_block_count > 0:
                        repeat_block_count -= 1
                        finished = False
            else:
                for Block in Blocks:
                    matched, finished = Block.match(code_line)
                    if matched:
                        current_Block = Block
                        break

            if finished:
                child_block = current_Block(self)
                child_block.compile(block_lines)

                child_blocks.append(child_block)

                current_Block = None
                block_lines = []
                repeact_block_count = 0

        return child_blocks

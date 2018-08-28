from .precompiler import precompile_file
from .blocks import ProgramBlock


def compile(f):
    code_lines = precompile_file(f)
    program_block = ProgramBlock(None)
    program_block.compile(code_lines)
    return program_block


def run(program_block: ProgramBlock):
    program_block.run()

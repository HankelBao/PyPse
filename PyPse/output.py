from lark import Tree
from .compiler import VERSION, WARNING_MODE


file_name = ""
current_block = None
current_line_num_start = None
current_line_num_end = None


def register_file_name(register_file_name: str):
    global file_name
    file_name = register_file_name


def register_current_block(register_current_block, block_token: Tree):
    global current_block, current_line_num_start, current_line_num_end
    current_block = register_current_block
    current_line_num_start = block_token.meta.line
    current_line_num_end = block_token.meta.end_line


class Messages():
    def output_welcome():
        global VERSION
        print(f"pypse {VERSION} (beta) - Pseudocode Compiler in Python")

    def loaded_file(file_name):
        print(f"pypse: compiling {file_name}...")

    def no_input_file():
        print("pypse: no input file")
        Messages.fatal()

    def unknown_argv(argv_str: str):
        print("pypse: unknown argv: {argv_str}")
        Messages.fatal()

    def finished():
        print("pypse: finished")

    def fatal():
        print("pypse: exit due to fatal error")
        exit()


class Warnings():
    def output(content: str):
        global current_block, current_line_num_start, current_line_num_end, WARNING_MODE
        print(WARNING_MODE)
        if WARNING_MODE:
            if current_line_num_end:
                print(f"line {current_line_num_start}~{current_line_num_end} {str(current_block)}: {content}")
            else:
                print(f"line {current_line_num_start}: {content}")


class Errors():
    def output(content: str):
        global current_block, current_line_num_start, current_line_num_end
        if current_line_num_end:
            print(f"line {current_line_num_start}~{current_line_num_end} {str(current_block)}: {content}")
        else:
            print(f"line {current_line_num_start}: {content}")
        Messages.fatal()

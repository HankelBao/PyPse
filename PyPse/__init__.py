from .parser import parse_file_to_token
from .blocks import RootBlock
from .debug import Debug


def pypse_run(file):
    token_tree = parse_file_to_token(file)
    print("Tokens:")
    print(token_tree.pretty())

    print("Program Output:")
    root_block = RootBlock(None)
    Debug.register_root_block(root_block)
    root_block.run(token_tree)
    print("")

    print("Program Debug Output:")
    root_block.recursive_debug_output()


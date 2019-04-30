from .parser import parse_file_to_token
from .blocks import RootBlock
from .debug import Debug, DebugOutput
from .compiler import WARNING_MODE
from .output import Messages


def pypse_run(file, DEBUG=False, WARNING=True):
    global WARNING_MODE
    WARNING_MODE = WARNING

    Messages.loaded_file(file.name)

    token_tree = parse_file_to_token(file)
    if DEBUG:
        DebugOutput.output("Tokens:")
        DebugOutput.output(token_tree.pretty())


    root_block = RootBlock(None)
    Debug.register_root_block(root_block)
    root_block.init_sys_symbols()
    root_block.run(token_tree)

    if DEBUG:
        DebugOutput.output("")
        DebugOutput.output("Structures:")
        root_block.recursive_debug_output()

    Messages.finished()

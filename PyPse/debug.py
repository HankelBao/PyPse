"""
Built for DebugBlock
"""
class Debug():
    RootBlock = None

    @staticmethod
    def register_root_block(root_block):
        Debug.RootBlock = root_block

    @staticmethod
    def get_root_block():
        return Debug.RootBlock


class DebugOutput():
    DebugOutputDepth = 0

    @staticmethod
    def output(content):
        DebugOutput.__print_spaces()
        print(content)

    @staticmethod
    def output_block_title(content):
        DebugOutput.__print_spaces()
        print(f"[{content}]")

    @staticmethod
    def output_block_attr(content):
        DebugOutput.__print_spaces()
        print(f"@{content}:")

    @staticmethod
    def increase_depth():
        DebugOutput.DebugOutputDepth += 2

    @staticmethod
    def decrease_depth():
        DebugOutput.DebugOutputDepth -= 2

    @staticmethod
    def __print_spaces():
        for i in range(DebugOutput.DebugOutputDepth):
            print(" ", end="")

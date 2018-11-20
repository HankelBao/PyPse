import sys, os
from enum import Enum, auto
from .compiler import pypse_run


class OptionType(Enum):
    DEBUG = auto()


def launch():
    print("PyPse 0.1.x (beta) - Pseudocode Compiler in Python")
    options = []

    if len(sys.argv) < 2:
        print("PyPse: no input file")
        exit()

    for argv in sys.argv:
        if argv[0:2] == "--":
            option_str = argv[2:]
            if option_str == "debug":
                options.append(OptionType.DEBUG)

    file_name = sys.argv[1]
    file_path = os.path.realpath(os.path.join(os.getcwd(), file_name))
    file = open(file_path, "r")

    if OptionType.DEBUG in options:
        pypse_run(file, DEBUG=True)
    else:
        pypse_run(file)

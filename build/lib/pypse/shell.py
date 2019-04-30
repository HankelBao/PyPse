import sys, os
from .output import Messages
from .pypse_run import pypse_run


def launch():
    options = {}

    if len(sys.argv) < 2:
        Messages.no_input_file()

    file_name = None
    for argv in sys.argv:
        if argv[0:2] == "--":
            option_str = argv[2:]
            if option_str == "debug":
                options['DEBUG'] = True
            if option_str == "nowarning":
                options['WARNING'] = False
        else:
            file_name = argv

    file_path = os.path.realpath(os.path.join(os.getcwd(), file_name))
    file = open(file_path, "r")

    options['file'] = file
    pypse_run(**options)

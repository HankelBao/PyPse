from PyPse import pypse_run


file = open("test.pse", "r")
pypse_run(file, DEBUG=True)

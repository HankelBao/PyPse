from pypse import pypse_run


file = open("test/test.5.pse", "r")
pypse_run(file, DEBUG=False, WARNING=False)

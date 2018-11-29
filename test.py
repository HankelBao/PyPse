from pypse import pypse_run


file = open("test/test.pse", "r")
pypse_run(file, DEBUG=True, WARNING=False)

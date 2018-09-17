from PyPse import PyPse_compile, PyPse_run

f = open("test.pse", "r")
pypse_bin = PyPse_compile(f)
PyPse_run(pypse_bin)
print() # For global breakpoints

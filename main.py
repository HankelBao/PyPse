from PyPse import compile as PyPse_compile
from PyPse import run as PyPse_run

f = open("test.pse", "w")
bin = PyPse_compile(f)
PyPse_run(bin)


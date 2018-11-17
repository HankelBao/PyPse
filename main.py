from PyPse import pypse_run

f = open("test.pse", "r")
pypse_run(f)
print()  # For global breakpoints

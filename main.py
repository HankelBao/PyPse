from PyPse import pypse_compile

f = open("test.pse", "r")
pypse_compile(f)
print()  # For global breakpoints

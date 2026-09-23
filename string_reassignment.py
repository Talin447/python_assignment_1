def change_str(s):
    s = "X" + s[1:]
    print("Inside function:", s)
s = "Hello"
change_str(s)
print("Outside function:", s)
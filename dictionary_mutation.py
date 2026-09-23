def add_entry(d, name, age):
    d[name] = age
a = {}
add_entry(a, "TALIN", 19)
add_entry(a, "PVK", 19)
print(a)
def reassign_dict(d):
    d = {"TALIN": 56, "PVK": 67}
    print("Inside function:", d)

reassign_dict(a)
print("Outside function:", a)

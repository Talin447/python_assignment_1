def max(a, b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = max(a, b)
print("Maximum number is:", c)
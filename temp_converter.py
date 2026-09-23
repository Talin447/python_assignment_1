def temp(c):
    f = (c * 9/5) + 32
    return f
c = float(input("Enter temperature in Celsius: "))
f = temp(c)
print("Temperature in Fahrenheit:", f)   
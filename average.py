nums = []
total = 0

for i in range(10):
    n = int(input("Enter number: "))
    nums.append(n)
    total += n

average = total / 10

print("Sum:", total)
print("Average:", average)

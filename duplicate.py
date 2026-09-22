nums = input("Enter numbers separated by space: ").split()

# Convert to integers manually
numbers = []
for x in nums:
    numbers.append(int(x))

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("List after removing duplicates:", unique)
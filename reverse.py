nums = input("Enter numbers separated by space: ").split()

# Convert to integers manually
numbers = []
for x in nums:
    numbers.append(int(x))

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
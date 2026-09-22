nums = []

for i in range(7):
    n = int(input("Enter number: "))
    nums.append(n)

smallest = nums[0]
largest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("Smallest:", smallest)
print("Largest:", largest)
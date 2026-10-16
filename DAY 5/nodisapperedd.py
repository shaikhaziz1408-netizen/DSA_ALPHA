# Find all numbers that disappered from the array

nums = [3, 0, 1, 7]

largest = nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]   # Largest element in array

# Find missing numbers
for i in range(largest + 1):
    count = 0                   # If number does not apper in the array, we will print the number

    for j in range(len(nums)):
        if nums[j] == i:
            count = count + 1

    if count == 0:
        print(i)
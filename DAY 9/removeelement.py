# Remove all occurrences of a given value from an array and return the remaining array.
nums = [3, 2, 2, 3]
val = 3

write = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[write] = nums[i]
        write = write + 1

result = [0] * write

for i in range(write):
    result[i] = nums[i]

print(result) 
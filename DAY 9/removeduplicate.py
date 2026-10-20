# Remove duplicates from sorted array using two pointer technique
nums = [1, 1, 2, 2, 3]

write = 1     # Keep 1st element as it is sorted array

for i in range(1, len(nums)):
    if nums[i] != nums[write - 1]:
        nums[write] = nums[i]      # new unique number
        write = write + 1

result = [0] * write             # move write position, for next unique number

for i in range(write):
    result[i] = nums[i]

print(result)
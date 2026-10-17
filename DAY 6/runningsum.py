# Running Sum of 1d Array
nums = [1, 2, 3, 4]
total = 0

for i in range(len(nums)):
    total = total + nums[i]
    nums[i] = total

print(nums)
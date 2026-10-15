# Running Sum of 1d Array
nums = [1, 2, 3, 4, 5 , 6]
total = 0

for i in range(len(nums)):
    total = total + nums[i]   # adds current element to total
    nums[i] = total           # replaces current element with total

print(nums)


# Leetcode Solution
class Solution:
    def runningSum(self, nums):
        n = len(nums)
        r = [0] * n
        total = 0
        for i in range(n):
            total = total + nums[i]
            r[i] = total
        return r
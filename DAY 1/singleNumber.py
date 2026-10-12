class Solution:
    def singleNumber(self, nums):
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] = seen[num] + 1
            else:
                seen[num] = 1

        for num in nums:
            if seen[num] == 1:
                return num
class Solution:
    def longestOnes(self, nums, k):
        left = 0                       # starting point of the window
        zeros = 0                      # count of zeros in the current window
        maxlength = 0                  # maximum length of the window found so far
        for right in range(len(nums)): 
            if nums[right] == 0:
                zeros += 1             # increase count of zeros
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            length = right - left + 1
            if length > maxlength:     # update maximum length if current window is larger
                maxlength = length
        return maxlength
nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = 2
obj = Solution()
print(obj.longestOnes(nums, k))
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        
        target = n - k    # Convert Kth largest into an index in ascending order
        low = 0
        high = n - 1

        while low <= high:
            pivot = nums[high]
            i = low - 1
            
            for j in range(low, high):    # Partition the array
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            
            nums[i + 1], nums[high] = nums[high], nums[i + 1]    # Place pivot in its correct position

            pivot_index = i + 1

            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                low = pivot_index + 1
            else:
                high = pivot_index - 1
        return -1

# Time Complexity
# Best Case: O(n)
# Average Case: O(n)
# Worst Case: O(n^2)

# Space Complexity
# Best Case: O(1)
# Average Case: O(1)
# Worst Case: O(1)
nums = [3, 1, 2, 4]

l = 0
r = len(nums) - 1

while l < r:
    # If left is odd and right is even, swap them
    if nums[l] % 2 != 0 and nums[r] % 2 == 0:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    else:
        # Move left pointer forward if already even
        if nums[l] % 2 == 0:
            l += 1
        # Move right pointer backward if already odd
        if nums[r] % 2 != 0:
            r -= 1

print(nums) 
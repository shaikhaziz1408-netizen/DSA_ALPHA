nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

n = len(nums)
k = k % n

# Reverse the entire array
left = 0
right = n - 1

while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    left = left + 1
    right = right - 1

# Reverse the first k elements
left = 0
right = k - 1

while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    left = left + 1
    right = right - 1

# Reverse the remaining elements
left = k
right = n - 1

while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    left = left + 1
    right = right - 1

print(nums)
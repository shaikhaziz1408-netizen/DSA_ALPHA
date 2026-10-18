nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

n = len(nums)

for i in range(0, n, k):
    left = i
    right = i + k - 1

    if right >= n:
        right = n - 1

    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

        left = left + 1
        right = right - 1

print(nums)
nums = [-4, -1, 0, 3, 10]

l = 0
r = len(nums) - 1
k = len(nums) - 1
res = [0] * len(nums)

while l <= r:
    left_sq = nums[l] * nums[l]
    right_sq = nums[r] * nums[r]

    if left_sq > right_sq:
        res[k] = left_sq
        l += 1
    else:
        res[k] = right_sq
        r -= 1
    k -= 1

print(res)  
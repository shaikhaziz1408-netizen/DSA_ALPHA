nums = [1, 2, 3, 1]
k = 3

window = {}
left = 0
result = False

for right in range(len(nums)):

    if right - left > k:
        del window[nums[left]]
        left += 1

    if nums[right] in window:
        result = True
        break

    window[nums[right]] = 1

print(result)
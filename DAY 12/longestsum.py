# To find the length of the longest continuous subarray whose sum equals k

k = 5
nums = [2, 3, 5, 1, 9]

l = 0
current_sum = 0
max_len = 0

for r in range(len(nums)):
    current_sum += nums[r]

    # Shrink if sum exceeds k
    while l <= r and current_sum > k:
        current_sum -= nums[l]
        l += 1

    # Check match
    if current_sum == k:
        window_size = r - l + 1
        if window_size > max_len:
            max_len = window_size

print(max_len)

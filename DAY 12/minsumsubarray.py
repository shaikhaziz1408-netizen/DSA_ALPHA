# To find the minimum length of a continuous subarray whose sum is greater than or equal to 7.
nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0                         # starting index of the sliding window
right = 0                        # ending index of the sliding window
current_sum = 0                  # Sum of elements inside window
min_length = len(nums) + 1

while right < len(nums):
    current_sum = current_sum + nums[right]

    while current_sum >= target:             # trying to make window smaller
        length = right - left + 1

        if length < min_length:
            min_length = length

        current_sum = current_sum - nums[left]
        left = left + 1

    right = right + 1

if min_length == len(nums) + 1:
    print(0)
else:
    print(min_length)

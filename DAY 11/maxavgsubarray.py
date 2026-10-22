# To find the maximum average of any contiguous subarray of length k.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4
 
subarray_sum = 0           # To store the sum of the current window

for i in range(k):
    subarray_sum = subarray_sum + nums[i]   # Sum of the first window

max_sum = subarray_sum               # Initial max sum

# Slide the window
for i in range(k, len(nums)):
    subarray_sum = subarray_sum - nums[i - k]             # Remove old element and its sum
    subarray_sum = subarray_sum + nums[i]                 # Add new element and its sum

    if subarray_sum > max_sum:
        max_sum = subarray_sum

avg = max_sum / k                  # average of maximum subarray
print(avg)

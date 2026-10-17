nums = [1, 2, 3, 4, 5]

n = len(nums)                
prefix = [0] * n     # To store the cummulative sum of array


prefix[0] = nums[0]        # Fisrt elemnt od prefix array is first element of array

for i in range(1, n):            # Calculate the prefix sum for each index
    prefix[i] = prefix[i - 1] + nums[i]    # Add the current element to the previous prefix sum

# Fixed range
left = 1
right = 3

# Calculate range sum
if left == 0:
    result = prefix[right]
else:
    result = prefix[right] - prefix[left - 1]

print(result)

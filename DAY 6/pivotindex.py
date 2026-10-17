# To find the pivot index
# Sum of array to left and right of index should be equal
nums = [1, 7, 3, 6, 5, 6]
total = 0

# Find the sum of all numbers in array++6
for i in range(len(nums)):
    total = total + nums[i]

left = 0         # Initialize left sum to 0
pivot = -1       # We have not found the pivot index yet

# Check each index
for i in range(len(nums)):
    right = total - left - nums[i]   

    if left == right:    # If left sum is equal to right sum, we have found the pivot index
        print(i)
        break

    left = left + nums[i]

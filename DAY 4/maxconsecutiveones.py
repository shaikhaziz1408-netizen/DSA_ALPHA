# To find the maximum number of consecutive 1's in an array of 0's and 1's
nums = [1, 1, 0, 1, 1, 1]
current = 0    
largest = 0    # consecutive count of 1's
for i in range(len(nums)):
    if nums[i] == 1:
        current = current + 1
    else:
        current = 0
    if current > largest:
        largest = current

print(largest)
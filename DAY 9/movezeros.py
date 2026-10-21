# Move all the zeros at the end while not changing the order of non zero numbers
# For this we will use 2 pointers, which are in same direction
# First pointer checks the elemnts, second one tells us where to put the next element
nums = [0, 1, 0, 3, 12]

write = 0      # Initialize the write pointer to 0, which will point to the index where the next non-zero element should be placed

for i in range(len(nums)):
    if nums[i] != 0:
        temp = nums[write]
        nums[write] = nums[i]   # current non-zero number at the write position.

        nums[i] = temp
        write = write + 1

print(nums)
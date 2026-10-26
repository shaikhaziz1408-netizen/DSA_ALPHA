# To sort a array using bubble sort
def bubbleSort(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:    #If the left number is bigger than the right number, we swap them.
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp        #swapping elements

    return nums

nums = [5, 2, 4, 1]
print(bubbleSort(nums))
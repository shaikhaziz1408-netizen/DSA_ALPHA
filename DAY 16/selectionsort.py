# To Sort array in ascending order
# By finding the smallest element in the unsorted portion and swapping it into the correct position.
def selectionSort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
    return nums
nums = [5, 3, 1, 4]
print(selectionSort(nums))
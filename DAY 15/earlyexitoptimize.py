# Sort an array in ascending order using Bubble Sort and stop early if a complete pass makes no swaps.
def bubbleSort(nums):
    n = len(nums)  

    for i in range(n - 1): 
        swapped = False  # Assume no swaps are needed in this pass

        for j in range(n - 1 - i):          # Compare adjacent elements
            if nums[j] > nums[j + 1]:       # Check if they are in the wrong order
                temp = nums[j]               
                nums[j] = nums[j + 1]        
                nums[j + 1] = temp   
                swapped = True  

        if swapped == False:  # Check if no swaps happened in the entire pass
            break  

    return nums 


nums = [1, 2, 3, 4, 5]
print(bubbleSort(nums)) 
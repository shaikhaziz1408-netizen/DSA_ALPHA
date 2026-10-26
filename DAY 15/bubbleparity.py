# Rearrange an array so that all even numbers appear before all odd numbers using Bubble Sort.
def sortArrayByParity(nums):
    n = len(nums)  

    for i in range(n - 1):  
        for j in range(n - 1 - i):  # Compare adjacent elements
            
            if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:   # Check if the left element is odd and the right is even
                temp = nums[j]                # Store the left element
                nums[j] = nums[j + 1]         # Move the even element to the left
                nums[j + 1] = temp            # Move the odd element to the right

    return nums 


nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))  
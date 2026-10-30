class Solution:
    def quickSort(self, arr, low, high):
        if low >= high:
            return
        
        pivot = arr[low]    # Choose the first element as the pivot
        lt = low
        i = low
        gt = high           # gt marks the boundary of elements greater than pivot

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1

            # If current element is greater than pivot, move greater element to the right section
            elif arr[i] > pivot:                
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        self.quickSort(arr, low, lt - 1)
        self.quickSort(arr, gt + 1, high)

# Time Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2)

# Space Complexity
# Best Case: O(log n)
# Average Case: O(log n)
# Worst Case: O(n)
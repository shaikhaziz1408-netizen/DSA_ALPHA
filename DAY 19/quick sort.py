class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]         # Choose the last element as the pivot
        i = low - 1

        for j in range(low, high):   # Traverse the array from low to high-1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]         # Place the pivot in its correct sorted position

        return i + 1

    def quickSort(self, arr, low, high):

        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)  # sort the left part of the pivot
            self.quickSort(arr, pi + 1, high) # sort the right part of the pivot

# Time Complexity
# Best Case: O(n log n) 
# Average Case: O(n log n) 
# Worst Case: O(n^2) 

# Space Complexity:
# Best Case: O(log n)
# Average Case: O(log n)
# Worst Case: O(n)
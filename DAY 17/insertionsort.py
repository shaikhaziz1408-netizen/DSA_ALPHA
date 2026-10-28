def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1          # To point to the element just before key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key   # To insert key into its correct sorted position
    return arr
nums = [5, 3, 4, 1, 2]
print(insertion_sort(nums))

# Time Complexity:
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)

# Space Complexity: O(1)
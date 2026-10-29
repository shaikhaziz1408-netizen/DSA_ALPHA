def merge_arrays(arr1, arr2):
    result = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):     # Compare elements from both arrays
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):              # Copy remaining elements from arr1
        result.append(arr1[i])
        i += 1

    while j < len(arr2):             # Copy remaining elements from arr2
        result.append(arr2[j])
        j += 1

    return result

arr1 = [1, 4, 7]
arr2 = [2, 3, 6, 8]

print(merge_arrays(arr1, arr2))

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2    # To find the mid of the array

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    # Merge both sorted halves
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy remaining left elements
    while i < len(left):
        result.append(left[i])
        i += 1

    # Copy remaining right elements
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


nums = [8, 3, 5, 2]
print(merge_sort(nums))

# Time Complexity: O(n log n)
# Space Complexity: O(n)
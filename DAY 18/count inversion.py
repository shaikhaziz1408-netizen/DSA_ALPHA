# An inversion is a pair of elements where a bigger element appears before a smaller element.
def count_inversions(nums):
    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2

    left, left_count = count_inversions(nums[:mid])
    right, right_count = count_inversions(nums[mid:])

    result = []
    i = 0
    j = 0
    count = left_count + right_count       # Count inversions from left and right halves

    # Merge the sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            count += len(left) - i
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result, count


nums = [2, 4, 1, 3, 5]

sorted_nums, total = count_inversions(nums)

print("Sorted array:", sorted_nums)
print("Inversion count:", total)

# Time Complexity: O(n log n)
# Space Complexity: O(n)
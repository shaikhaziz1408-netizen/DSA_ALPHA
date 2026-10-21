# Setup inputs
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# Pointers
i = m - 1          # Last element in nums1's valid data
j = n - 1          # Last element in nums2
k = m + n - 1      # Insertion position from the end

while j >= 0:
    if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
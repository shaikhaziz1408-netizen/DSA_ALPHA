# To find mean of array after removing some elements from the array.

arr = [6, 2, 7, 5, 1, 2, 0, 2, 6, 3,
       4, 5, 1, 2, 3, 4, 5, 6, 7, 8]

n = len(arr)

# Sort using Bubble Sort
for i in range(n):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Calculate elements to remove
remove = n // 20

total = 0
count = 0

# Add only the middle elements
for i in range(remove, n - remove):
    total = total + arr[i]
    count = count + 1

mean = total / count
print(mean)

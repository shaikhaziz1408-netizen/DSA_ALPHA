nums = [3, 0, 1]
n = len(nums)

for i in range(n + 1):
    count = 0

    for j in range(n):
        if nums[j] == i:
            count = count + 1

    if count == 0:
        print(i)
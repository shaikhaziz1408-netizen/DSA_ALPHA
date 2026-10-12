# two_sum problem
# brute force
nums = [2, 4, 6, 8, 10, 12]
target = 10
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums [j] == target:
            print(nums[i],nums[j])




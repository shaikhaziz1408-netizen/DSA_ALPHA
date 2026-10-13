# Problem - To find out maximum number in an array
# Assume first number is largest initially 
# Then compare each element with the largest element and change the largest element according to array 
num = [34, 56, 12, 15, 11, 111]

largest = num[0]

for i in num:
    if i > largest:
        largest = i

print(largest)



# Method 1 - Using two arrays

num = [34, 56, 12, 15, 11, 111]    
rev = [0] * len(num)               #Empty array of same length as num

for i in range(len(num)):            
    rev[i] = num[len(num) - 1 - i]  #read the elements of num in reverse order and store them in rev

print(rev)

#Space complexity - O(n)




# Method 2 - Swapping elements
num = [34, 56, 12, 13, 15, 11, 111]

left = 0                  # Start from the first index
right = len(num) - 1      # Start from the last 

while left < right:
    temp = num[left]      # Temprorily store left element 
    num[left] = num[right] # moving right element to left
    num[right] = temp     # Temporarily stored element(left element) to right

    left = left + 1       # Move left index forward
    right = right - 1     # Move right index backward

print(num)

#Space complexity - O(1)

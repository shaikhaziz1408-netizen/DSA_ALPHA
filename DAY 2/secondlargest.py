num = [34, 56, 12, 15, 11, 111]

first = num[0]   # Assume the first element is the largest
second = num[0]

for n in num:
    if n > first:
        second = first    #Largest number becomes second largest
        first = n         #largest number is updated
    elif n > second and n != first:
        second = n        
  
print(second)
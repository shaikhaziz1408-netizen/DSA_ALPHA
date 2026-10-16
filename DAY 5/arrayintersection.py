# Intersection of two arrays
array1 = [1, 2, 2, 3, 4]
array2 = [2, 3, 5, 6, 2]

intersection = []

for i in array1:
    for j in array2:
        if i == j:
            count = 0

            for item in intersection:
              if item == i:                      # If the element is already present increase count
                count = count + 1
                             
            if count == 0:                       # Add the element to intersection if it is not already present
                intersection = intersection + [i]

print(intersection)
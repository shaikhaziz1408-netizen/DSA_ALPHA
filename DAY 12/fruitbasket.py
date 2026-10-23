# We have only 2 baskets, and each basket can hold only one type of fruit.
# We can collect fruits only from a continuous section of the array.
fruits = [1, 2, 3, 2, 2]

basket = {}
l = 0
max_fruits = 0

for r in range(len(fruits)):
    fruit = fruits[r]
    if fruit in basket:
        basket[fruit] += 1
    else:
        basket[fruit] = 1

    # Shrink from left if more than 2 distinct fruit types
    while len(basket) > 2:
        left_fruit = fruits[l]
        basket[left_fruit] -= 1
        if basket[left_fruit] == 0:
            del basket[left_fruit]
        l += 1

    # Valid window with at most 2 fruit types
    window_size = r - l + 1          # If this length is greater than the previous maximum, update max_fruits.
    if window_size > max_fruits:
        max_fruits = window_size

print(max_fruits)  
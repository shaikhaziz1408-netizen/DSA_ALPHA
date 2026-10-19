 # Reversing a string using two pointers
chars = ["h", "e", "l", "l", "o"]

left = 0
right = len(chars) - 1

while left < right:
    temp = chars[left]                # Temporary variable to store the value of the left character
    chars[left] = chars[right]        # Swapping the left character with the right character
    chars[right] = temp               # Swapping the right character with the temporary variable

    left = left + 1
    right = right - 1

print(chars)
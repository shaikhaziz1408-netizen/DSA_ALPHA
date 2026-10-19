# Palindrome Check
a = "racecar"

left = 0
right = len(a) - 1
is_palindrome = True

while left < right:
    if a[left] != a[right]:       #Checking first and last character
        is_palindrome = False

    left = left + 1
    right = right - 1

print(is_palindrome)
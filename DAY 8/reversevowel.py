# To reverse the vowels in a string using two pointers
s = "hello"
chars = list(s)
vowels = "aeiouAEIOU"

left = 0
right = len(chars) - 1

while left < right:
    if chars[left] not in vowels:
        left = left + 1

    elif chars[right] not in vowels:
        right = right - 1

    else:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left = left + 1
        right = right - 1

result = ""

for i in range(len(chars)):
    result = result + chars[i]

print(result)
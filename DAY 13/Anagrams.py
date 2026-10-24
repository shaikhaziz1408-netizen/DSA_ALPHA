s = "cbaebabacd"
p = "abc"

target = {}
window = {}
left = 0

result = [0] * len(s)
count = 0

for i in range(len(p)):
    if p[i] in target:
        target[p[i]] += 1
    else:
        target[p[i]] = 1

for right in range(len(s)):

    if s[right] in window:
        window[s[right]] += 1
    else:
        window[s[right]] = 1

    if right - left + 1 > len(p):
        window[s[left]] -= 1

        if window[s[left]] == 0:
            del window[s[left]]

        left += 1

    if right - left + 1 == len(p):
        if window == target:
            result[count] = left
            count += 1

i = 0
while i < count:
    print(result[i], end=" ")
    i += 1
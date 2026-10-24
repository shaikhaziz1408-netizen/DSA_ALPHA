s1 = "ab"
s2 = "eidbaooo"

target = {}
window = {}
left = 0
result = False

for i in range(len(s1)):
    if s1[i] in target:
        target[s1[i]] += 1
    else:
        target[s1[i]] = 1

for right in range(len(s2)):

    if s2[right] in window:
        window[s2[right]] += 1
    else:
        window[s2[right]] = 1

    if right - left + 1 > len(s1):
        window[s2[left]] -= 1

        if window[s2[left]] == 0:
            del window[s2[left]]

        left += 1

    if right - left + 1 == len(s1):
        if window == target:
            result = True
            break

print(result)
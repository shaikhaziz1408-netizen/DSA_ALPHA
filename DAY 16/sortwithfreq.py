def sortwithFre(s):
    freq = {}
    # Count the frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    chars = list(freq.keys())
    n = len(chars)
    # Sort characters by frequency in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if freq[chars[j]] > freq[chars[i]]:
                chars[i], chars[j] = chars[j], chars[i]

    result = ""
    # Repeat each character according to its frequency
    for ch in chars:
        result += ch * freq[ch]
    return result
s = "mississippi"
print(sortwithFre(s))
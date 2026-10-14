# Count Frequencies of Array Elements
nums = [10, 20, 10, 30, 20, 10]
freq = {}

for n in nums:
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1

for n in freq:
    print(n, "--", freq[n],)

#hashmap counting

nums = [2, 2, 1, 1, 2, 2, 2]
freq = {}

for n in nums:
    if n in freq:
        freq[n] = freq[n] + 1   # if number repeats increase the count
    else:
        freq[n] = 1             # If the number is new, add to dictionary with count 1

for n in freq:
    if freq[n] > len(nums) // 2:
        print(n)


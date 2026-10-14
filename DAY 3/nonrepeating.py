# Find the first non-repeating number in a list
# create a empty dictionary to store frequency of numbers
# Traverse list and count frequency of each number, if the frequency is 1, print the number
nums = [4, 5, 1, 2, 1, 4, 5]
freq = {}

for n in nums:
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1

for n in nums:
    if freq[n] == 1:
        print(n)


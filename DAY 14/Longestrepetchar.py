class Solution:
    def characterReplacement(self, s, k):
        left = 0               # starting point of the window
        maxfreq = 0            # maximum frequency of any character in the current window
        maxlength = 0          # maximum length of the window found so far
        count = {}             
        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            if count[ch] > maxfreq:
                maxfreq = count[ch]
            while (right - left + 1) - maxfreq > k:  # if the number of characters to change exceeds k shrink the window
                old = s[left]             
                count[old] -= 1
                left += 1
            length = right - left + 1   # calculate the length of the current window
            if length > maxlength:      # update the maximum length if the current window is longer

                maxlength = length
        return maxlength
s = "AABABBA"
k = 1
obj = Solution()
print(obj.characterReplacement(s, k))
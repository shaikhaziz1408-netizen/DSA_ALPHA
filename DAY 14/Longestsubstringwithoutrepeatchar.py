class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0                   # starting point of the window
        maxlength = 0              # maximum length of the window found so far
        last_seen = {}             # Stores each character's latest index
        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen and last_seen[ch] >= left: # Check if the character appeared inside the current window
                left = last_seen[ch] + 1
            last_seen[ch] = right      # Update the latest index of this character
            length = right - left + 1  # Calculate the length of the current window
            if length > maxlength:
                maxlength = length
        return maxlength
s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
# Time complexity: O(n) length of the string
# Space complexity: O(m) length of unique chars

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        seenChars = set()

        for right in range(len(s)):
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1
            seenChars.add(s[right])
            length = max(length, right - left + 1)
        
        return length

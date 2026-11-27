# n chars in string s
# m unique chars in string s

# Time complexity: O(n)
# Space complexity: O(m)

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = maxFreq = result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result
# Time complexity: O(n * m)
# Space complexity: O(m)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        uniqueChars = set(s)

        for char in uniqueChars:
            count = left = 0

            for right in range(len(s)):
                if s[right] == char:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                
                result = max(result, right - left + 1)
        
        return result
# Time complexity: O(n)
# Space complexity: O(n)

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        diffHash = defaultdict(int)
        for index in range(len(s)):
            diffHash[s[index]] += 1
            diffHash[t[index]] -= 1

        for value in diffHash.values():
            if value != 0: return False

        return True
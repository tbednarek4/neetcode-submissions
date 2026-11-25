# n = len(strs) and m = [max(len(str)) for str in strs]
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seenStrs = defaultdict(list)
        for string in strs:
            freqList = 26 * [0]
            for char in string:
                freqList[ord(char) - ord('a')] += 1
            freqTuple = tuple(freqList)
            if freqTuple in seenStrs:
                seenStrs[freqTuple].append(string)
            else:
                seenStrs[freqTuple] = [string]
        
        return list(seenStrs.values())
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count
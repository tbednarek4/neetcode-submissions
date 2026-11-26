# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        for index in range(32):
            bit = (n >> index) & 1
            reversed += (bit << (31 - index))
        return reversed
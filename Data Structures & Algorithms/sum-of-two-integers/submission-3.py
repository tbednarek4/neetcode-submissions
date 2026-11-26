# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum = 0
        carry = 0

        for index in range(32):
            bit_a = (a >> index) & 1
            bit_b = (b >> index) & 1
            bit_sum = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (carry & (bit_a | bit_b))
            sum += (bit_sum << index)

        if sum > 0x7FFFFFFF:
            sum = ~(sum ^ 0xFFFFFFFF)

        return sum
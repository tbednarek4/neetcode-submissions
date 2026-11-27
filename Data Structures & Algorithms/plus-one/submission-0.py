# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits.copy()
        result.reverse()

        carry = 1
        for index in range(len(result)):
            result[index] += carry
            carry = result[index] // 10
            result[index] %= 10

        if carry > 0:
            result.append(carry)

        result.reverse()
        return result
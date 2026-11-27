# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            if temp == 1:
                return True
            n = temp
        return False
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        results = [0] * (n + 1)

        for num in range(1, n + 1):
            if offset * 2 == num:
                offset = num
            
            results[num] = 1 + results[num - offset]

        return results
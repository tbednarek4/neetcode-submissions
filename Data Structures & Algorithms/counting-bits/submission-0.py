class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for num in range(0, n + 1):
            results.append(bin(num).count('1'))
        return results
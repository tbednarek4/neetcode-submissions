# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        freqs = [[] for _ in range(len(nums))]
        for num, cnt in counts.items():
            freqs[cnt - 1].append(num)
        
        results = []
        for index in range(len(nums) - 1, -1, -1):
            for element in freqs[index]:
                results.append(element)
                if len(results) == k:
                    return results
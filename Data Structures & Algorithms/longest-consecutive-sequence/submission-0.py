# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        hashMap = {}

        for num in nums:
            if num not in hashMap:
                left = hashMap.get(num - 1, 0)
                right = hashMap.get(num + 1, 0)
                length = 1 + left + right
                hashMap[num] = hashMap[num - left] = hashMap[num + right] = length
                longestSequence = max(longestSequence, length)

        return longestSequence
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = count = result = maxCount = 0

        for right in range(len(nums)):
            count += nums[right]
            maxCount = max(maxCount, count)

            if (right - left + 1) - maxCount > k:
                count -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        max_volume = 0
        right = len(heights) - 1

        while left < right:
            min_height = min(heights[left], heights[right])
            max_volume = max(max_volume, (right - left) * min_height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_volume
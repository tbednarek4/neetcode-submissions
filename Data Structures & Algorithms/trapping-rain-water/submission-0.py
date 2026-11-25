# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        rainwater = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                rainwater += (left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                rainwater += (right_max - height[right])

        return rainwater
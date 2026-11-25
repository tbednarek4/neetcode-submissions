# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [-1] # defining a monotonic stack

        for index in range(len(heights)):
            # when the current height is lower than the max (last) from the stack
            while heights[index] < heights[stack[-1]] and stack[-1] != -1:
                currentIndex = stack.pop() # pop from the stack
                maxArea = max(maxArea, heights[currentIndex] * (index - 1 - stack[-1]))
            stack.append(index) # push into the stack the new max
        
        while stack[-1] > -1: # peek into the stack
            currentIndex = stack.pop()
            maxArea = max(maxArea, heights[currentIndex] * (len(heights) - 1 - stack[-1]))

        return maxArea
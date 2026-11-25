# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingDict = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in closingDict:
                if not stack or stack[-1] != closingDict[char]: return False
                else: stack.pop()
            else: stack.append(char)

        return len(stack) == 0
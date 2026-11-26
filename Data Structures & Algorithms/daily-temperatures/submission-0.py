# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)
        
        for index in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                temp = stack.pop()
                result[temp] = index - temp

            stack.append(index)

        return result
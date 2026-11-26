# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()  # Right operand
                a = stack.pop()  # Left operand

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # Truncates toward zero
            else:
                stack.append(int(token))

        return stack[0]
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])

        for i in range(1, height):
            for j in range(i):
                if i == j: continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(height):
            for j in range(width // 2):
                matrix[i][j], matrix[i][width - j - 1] = matrix[i][width - j - 1], matrix[i][j]
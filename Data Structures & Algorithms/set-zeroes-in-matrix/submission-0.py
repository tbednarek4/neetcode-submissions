# Time complexity: O(m * n)
# Space complexity: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        height = len(matrix)
        width = len(matrix[0])

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0: rowZero = True
                    else: matrix[i][0] = 0

        for i in range(1, height):
            for j in range(1, width):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(height):
                matrix[i][0] = 0

        if rowZero:
            for j in range(width):
                matrix[0][j] = 0
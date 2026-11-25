# Time complexity: O(n^2)
# Space complexity: O(n^2)

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols, squares = (defaultdict(set) for _ in range(3))

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue
                sq = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in squares[sq]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[sq].add(val)

        return True
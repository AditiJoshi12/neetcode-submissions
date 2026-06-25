class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row = [c for c in row if c != "."]
            if len(set(row)) != len(row):
                return False

        for i in range(9):
            col = [row[i] for row in board]
            col = [c for c in col if c != "."]
            if len(set(col)) != len(col):
                return False

        for i in range(3):
            for j in range(3):
                subBox = [board[r][c] for r in range(3*i, 3*i+3) for c in range(3*j, 3*j+3)]
                subBox = [c for c in subBox if c != "."]
                if len(set(subBox)) != len(subBox):
                    return False

        return True
        
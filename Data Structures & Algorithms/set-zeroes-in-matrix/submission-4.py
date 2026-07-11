class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = [0]*m, [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(m):
            if rows[i] == 1:
                matrix[i] = [0]*n

        for j in range(n):
            if cols[j] == 1:
                for i in range(m):
                    matrix[i][j] = 0

        
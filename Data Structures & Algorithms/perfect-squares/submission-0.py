class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1]*(n+1)
        dp[0] = 0

        squares = [j*j for j in range(1, int(n**0.5) + 1)]

        for i in range(1, n+1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)

        return dp[-1] 
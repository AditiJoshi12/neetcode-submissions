class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        a, b = 1, 2

        for i in range(2, n):
            prev = a 
            a = b
            b = prev + a

        return b
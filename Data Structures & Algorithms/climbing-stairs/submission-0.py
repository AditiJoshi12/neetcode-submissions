class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        path1, path2 = 1, 2

        for i in range(n-2):
            curr = path1 + path2
            path1 = path2
            path2 = curr

        return path2 


        
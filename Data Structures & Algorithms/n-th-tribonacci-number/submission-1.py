class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1 
            
        a, b, c = 0, 1, 1

        for i in range(2, n):
            t0, t1 = b, c
            c = a + b + c 
            b = t1
            a = t0

        return c
        
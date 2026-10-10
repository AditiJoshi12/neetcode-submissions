class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        q, rem = divmod(n, 3)

        if rem == 0: 
            return 3 ** q
        if rem == 1:
            return (3 ** (q-1)) * 4
        else:
            return 2 * 3 ** q

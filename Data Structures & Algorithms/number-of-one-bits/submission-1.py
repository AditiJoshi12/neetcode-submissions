class Solution:
    def hammingWeight(self, n: int) -> int:
        numOnes = 0

        while n > 0:
            n = n & (n-1)
            numOnes += 1

        return numOnes
            
        
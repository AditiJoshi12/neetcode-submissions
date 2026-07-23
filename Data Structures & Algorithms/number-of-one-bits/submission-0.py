class Solution:
    def hammingWeight(self, n: int) -> int:
        numOnes = 0

        while n > 0:
            numOnes += n & 1
            n = n >> 1 

        return numOnes
            
        
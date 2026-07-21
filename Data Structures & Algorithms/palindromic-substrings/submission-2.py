class Solution:
    def countSubstrings(self, s: str) -> int:   
        n = len(s)        
        numPals = 0

        for i in range(n):
            # odd palindromes 
            l, r = i, i
            while l>=0 and r<n and s[l] == s[r]:
                numPals += 1 
                l -= 1
                r += 1

            # even palindromes 
            l, r = i-1, i
            while l>=0 and r<n and s[l] == s[r]:
                numPals += 1
                l -= 1
                r += 1
        
        return numPals



        
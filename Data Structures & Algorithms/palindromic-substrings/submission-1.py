class Solution:
    def countSubstrings(self, s: str) -> int:    
        double = []
        n = len(s)

        for i in range(1, n):
            if s[i] == s[i-1]:
                double.append(i)
        
        numPals = n + len(double)

        for i in range(1, n):
            if i in double:
                r = 1 
                while i-1-r >= 0 and i+r < n and s[i-1-r] == s[i+r]:
                    numPals += 1
                    r += 1
            
            r = 1 
            while i-r >= 0 and i+r < n and s[i-r] == s[i+r]:
                numPals += 1
                r += 1
        
        return numPals



        
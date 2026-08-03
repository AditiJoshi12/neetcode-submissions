class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0
        double_pal = []
        n = len(s)

        for i in range(n-1):
            if s[i] == s[i+1]:
                double_pal.append(i)
        
        for i in range(n):
            j = 1
            while i - j > -1 and i + j < n:
                if s[i-j] == s[i+j]:
                    j += 1
                else:
                    break
            
            j -= 1
            
            if 2*j + 1 > max_len:
                max_len = 2*j + 1
                start = i-j

        for i in double_pal:
            j = 1
            while i - j > -1 and i + 1 + j < n:
                if s[i-j] == s[i+1+j]:
                    j += 1
                else:
                    break
            
            j -= 1
            
            if 2*j + 2 > max_len:
                max_len = 2*j + 2
                start = i-j
        
        result = s[start:start+max_len]
        
        return result
        
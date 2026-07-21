class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp2, dp1 = 1, 1

        for i in range(1, len(s)):
            currentWays = 0

            if s[i] != '0':
                currentWays += dp1
            
            two_digit = s[i-1:i+1]
            if 10 <= int(two_digit) <= 26:
                currentWays += dp2

            dp2 = dp1 
            dp1 = currentWays

        return dp1 
        
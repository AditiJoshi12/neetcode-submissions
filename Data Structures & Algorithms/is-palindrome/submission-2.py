class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        i = 0
        j = n-1

        while i < j :
            while i < j and not s[i].isalnum():
                i = i+1
                continue
            
            while i < j and not s[j].isalnum():
                j = j-1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i = i+1
            j = j-1

        return True
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        left, right = 0, 1
        max_len = 0

        while right <= n:
            chars = set(s[left:right])
            if len(chars) == right - left:
                max_len = max(max_len, right - left)
                right += 1
            else:
                left += 1

        return max_len
        
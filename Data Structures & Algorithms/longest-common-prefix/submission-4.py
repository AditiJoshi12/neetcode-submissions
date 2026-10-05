class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        lcp = ""

        for i, letter in enumerate(strs[0]):
            for word in strs:
                if word[i] != letter:
                    return lcp
            lcp += letter            

        return lcp
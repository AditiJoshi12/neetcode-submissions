class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        lcp = ""

        for i in range(len(strs[0])):
            k = strs[0][:i+1]
            for s in strs[1:]:
                if s[:i+1] != k:
                    return lcp 
            lcp = k

        return lcp
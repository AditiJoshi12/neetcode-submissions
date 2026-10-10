class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n1, n2 = len(word1), len(word2)
        m = min(n1, n2)

        for i in range(m):
            s += word1[i] + word2[i]


        return s + word1[m:] + word2[m:]
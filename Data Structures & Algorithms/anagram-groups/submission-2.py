class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in pairs:
                pairs[key] = []
            pairs[key].append(s)

        res = []

        for key in pairs:
            res.append(pairs[key])

        return res
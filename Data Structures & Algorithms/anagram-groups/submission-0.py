class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs: 
            key = "".join(sorted(str))
            if key not in hash:
                hash[key] = []
            hash[key].append(str)
        
        groupedAnagrams = []
        for key in hash:
            groupedAnagrams.append( hash[key] )

        return groupedAnagrams

        
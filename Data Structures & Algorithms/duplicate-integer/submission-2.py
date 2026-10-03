class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            if freq.get(num, 0) > 0:
                return True 
            
            freq[num] = freq.get(num, 0) + 1

        return False
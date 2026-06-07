class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        n = len( nums )
        
        for i in range(n):
            if target - nums[i] in num_index: 
                j = num_index[target - nums[i]]
                if i != j:
                    return [ min(i, j), max(i, j)] 

            num_index[nums[i]] = i
            
            
        
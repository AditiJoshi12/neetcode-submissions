class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
                return result
            
            subset.append(nums[index])
            backtrack(index+1)

            subset.pop()
            backtrack(index+1)

        backtrack(0)
        return result

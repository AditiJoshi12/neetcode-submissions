class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        subsets = []
        n = len(nums)

        def backtrack(remaining: int, start_index: int, path: List[int]):
            if remaining == 0:
                subsets.append(list(path))
                return

            for i in range(start_index, n): 
                if nums[i] > remaining:
                    break
                
                path.append(nums[i])
                backtrack(remaining - nums[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return subsets
        
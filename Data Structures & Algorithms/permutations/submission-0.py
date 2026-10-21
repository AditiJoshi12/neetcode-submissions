class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        n = len(nums)

        def backtrack():
            if len(subset) == n:
                results.append(subset.copy())
                return

            for num in nums:
                if num in subset: 
                    continue
                else:
                    subset.append(num)
                    backtrack()
                    subset.pop()

        backtrack()

        return results
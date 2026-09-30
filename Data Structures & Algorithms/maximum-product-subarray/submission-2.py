class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for num in nums[1:]: 
            temp = max_prod
            max_prod = max(num, max_prod*num, min_prod*num)
            min_prod = min(num, temp*num, min_prod*num)

            res = max(res, max_prod)

        return res

        
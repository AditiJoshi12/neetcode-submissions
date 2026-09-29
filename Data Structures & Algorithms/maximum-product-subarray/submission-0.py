class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curr_max, curr_min = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            temp_max = max(curr_max*num, num, curr_min*num)
            curr_min = min(curr_min*num, num, curr_max*num)
            curr_max = temp_max

            res = max(curr_max, res)

        return res


        
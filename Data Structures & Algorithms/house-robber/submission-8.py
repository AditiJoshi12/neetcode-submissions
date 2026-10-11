class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        h1 = nums[0]
        h2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            h = max(h1 + nums[i], h2)
            h1 = h2
            h2 = h

        return h2 # max(h1, h2)
        
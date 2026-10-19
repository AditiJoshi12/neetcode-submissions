class Solution:
    def rob(self, nums: List[int]) -> int:   
        if len(nums) == 1:
                return nums[0]     

        def rob_normal(arr): 
            if len(arr) == 1:
                return arr[0]

            r1 = arr[0]
            r2 = max(arr[0], arr[1])

            for p in arr[2:]:
                r = max(p+r1, r2)
                r1 = r2
                r2 = r

            return r2

        return max(rob_normal(nums[:-1]), rob_normal(nums[1:]))
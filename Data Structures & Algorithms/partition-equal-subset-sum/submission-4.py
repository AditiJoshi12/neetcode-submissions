class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False 

        target = sum(nums) // 2
        n = len(nums)

        dp = [False]*(target + 1)
        dp[0] = True

        for num in nums:
            if num > target:
                return False 

            for s in range(target, num-1, -1):
                dp[s] = dp[s] or dp[s-num]

            if dp[-1]:
                return True
            
        return dp[-1]

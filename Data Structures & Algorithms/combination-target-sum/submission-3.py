class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        nums.sort()

        for c in nums:
            for i in range(c, target+1):
                for combo in dp[i-c]:
                    dp[i].append(combo + [c])

        return dp[-1]
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        minlen = float("inf")
        currSum = 0 

        for r in range(n):
            currSum += nums[r]

            while currSum >= target:
                minlen = min(minlen, r-l+1)
                currSum -= nums[l]
                l += 1

        return minlen if minlen != float('inf') else 0
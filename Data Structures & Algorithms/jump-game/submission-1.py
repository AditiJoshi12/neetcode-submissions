class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)

        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if i >= n-1:
                return True

        return farthest >= n-1

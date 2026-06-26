class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        maxLeft = [0]*n
        maxRight = [0]*n

        maxLeft[0] = heights[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], heights[i])

        maxRight[n-1] = heights[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], heights[i])

        total = 0

        for i in range(n):
            total += min(maxLeft[i], maxRight[i]) - heights[i]

        return total
        
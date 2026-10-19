class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        c1, c2 = 0, 0

        for i in range(2, len(costs)+1):
            c = min(c1 + costs[i-1], c2+costs[i-2])
            c2 = c1
            c1 = c

        return c1
                    
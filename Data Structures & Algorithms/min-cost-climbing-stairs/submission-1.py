class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        c = [float("inf")]*(len(costs)+1)
        c[0] = c[1] = 0 

        for i in range(2, len(costs)+1):
            c[i] = min(c[i-1] + costs[i-1], c[i-2]+costs[i-2])

        return c[-1]
                    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 

        hold = -prices[0]
        sold = 0
        rest = 0

        for p in prices[1:]:
            prev_hold = hold
            hold = max(prev_hold, rest - p)
            rest = max(rest, sold)
            sold = prev_hold + p

        return max(rest, sold)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_price = prices[0]
        max_profit = 0

        for i in range(1, n):
            buy_price = min(prices[i], buy_price)

            profit = prices[i] - buy_price
            max_profit = max(profit, max_profit)

        return max_profit

            

            
        
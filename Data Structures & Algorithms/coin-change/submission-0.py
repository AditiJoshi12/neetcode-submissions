class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 

        amounts = [float("inf")]*(amount+1)
        amounts[0] = 0 

        for coin in coins:
            for i in range(coin, amount+1):
                amounts[i] = min(amounts[i], amounts[i-coin]+1)

        return amounts[-1] if amounts[-1] != float("inf") else -1
                 

        
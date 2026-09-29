class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        total, result = 0, 0
        n = len(gas)
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i+1

        return result
        
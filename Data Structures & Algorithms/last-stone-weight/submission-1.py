class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            st1, st2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if abs(st1-st2) != 0:
                heapq.heappush(stones, -abs(st1-st2))

        return -heapq.heappop(stones) if stones else 0
        
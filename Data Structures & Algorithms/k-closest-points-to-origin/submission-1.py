class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestK = []

        for x, y in points:        
            dist = x**2 + y**2
            heapq.heappush(closestK, (-dist, [x, y]))
            if len(closestK) > k:
                heapq.heappop(closestK)

        return [point for dist, point in closestK]
        
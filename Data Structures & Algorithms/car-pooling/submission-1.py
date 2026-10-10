class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        incar = []
        trips.sort(key=lambda c : c[1])

        for count, start, end in trips:
            heapq.heappush(incar, (end, count))
            capacity -= count 

            while incar and incar[0][0] <= start:
                _, numP = heapq.heappop(incar)
                capacity += numP

            if capacity < 0:
                return False

        return True
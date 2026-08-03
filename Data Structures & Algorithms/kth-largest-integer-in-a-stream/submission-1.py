class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxK =  nums
        self.k = k
        heapq.heapify(self.maxK)
            
        while len(self.maxK) > k:
            heapq.heappop(self.maxK)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxK, val)
        
        if len(self.maxK) > self.k:
                heapq.heappop(self.maxK)
        return self.maxK[0]
        

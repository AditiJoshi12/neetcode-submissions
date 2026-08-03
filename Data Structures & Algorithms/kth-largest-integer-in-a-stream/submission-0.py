class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxK =  []
        self.k = k

        for i in range(len(nums)):
            heapq.heappush(self.maxK, nums[i])
            
            if len(self.maxK) > k:
                heapq.heappop(self.maxK)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxK, val)
        
        if len(self.maxK) > self.k:
                heapq.heappop(self.maxK)
        return self.maxK[0]
        

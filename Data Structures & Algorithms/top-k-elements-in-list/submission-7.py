class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freqs = list(freq.values())
        oppFreq = {}
        for f in freq:
            if freq[f] not in oppFreq:
                oppFreq[freq[f]] = []
            oppFreq[freq[f]].append(f)

        heap = freqs[:k]
        heapq.heapify(heap)

        for f in freqs[k:]:
            if f > heap[0]: 
                heapq.heappop(heap)
                heapq.heappush(heap, f)
        
        res = [] 

        for f in heap: 
            res.append(oppFreq[f].pop())

        return res
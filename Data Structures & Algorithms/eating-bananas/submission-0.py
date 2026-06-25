class Solution:
    def canEat(self, piles, k):
        hours = 0
        
        for pile in piles:
            hours += (pile + k - 1)//k

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right)//2
            h_mid = self.canEat(piles, mid)

            if h_mid <= h:                 
                right = mid - 1
            else:
                left = mid + 1

        return left
        
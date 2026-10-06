class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 :
            return x

        # now binary search between 0 and n/2 
        left, right = 2, x/2 
        ans = 1

        while left <= right:
            mid = left + (right-left)//2 
            mid_sq = mid**2 

            if mid_sq == x:
                return int(mid)
            elif mid_sq < x: 
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return int(ans)

        


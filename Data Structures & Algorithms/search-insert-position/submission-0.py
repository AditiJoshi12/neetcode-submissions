class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1 

        while l <= r:
            mid = l + (r-l)//2 
            nmid = nums[mid]

            if nmid == target:
                return mid  
            elif nmid > target:
                r = mid - 1
            else:
                l = mid + 1

        return l
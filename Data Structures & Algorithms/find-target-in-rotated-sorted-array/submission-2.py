class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        inflection = left
        print(f'Inflection:{inflection}')

        if nums[0] <= target <= nums[inflection-1]:
            left, right = 0, inflection-1

        if nums[inflection] <= target <= nums[-1]:
            left, right = inflection, len(nums)-1

        print(f'left:{left}; right:{right}')
        print(nums)
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return -1

        
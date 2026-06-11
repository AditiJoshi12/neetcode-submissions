class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        n = len(nums)

        for i in range(n):
            #check if this number is the starting of the sequence
            if nums[i]-1 not in num_set:
                streak = 1
                while nums[i] + streak in  num_set:
                    streak = streak + 1
                
                longest_streak = max(streak, longest_streak)
        
        return longest_streak


        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}
        n = len(nums)

        for i, num in enumerate(nums):
            if num in freq:
                freq[num].append(i)
            else:
                freq[num] = [i]

        for i, num in enumerate(nums):
            if target - num == num and len(freq[num]) > 1:
                return freq[num]
            elif target - num != num and target - num in freq: 
                return [freq[num][0], freq[target - num][0]]

        
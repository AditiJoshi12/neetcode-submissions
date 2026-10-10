class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = math.floor(len(nums)/3)

        freq = {}
        ans = set()

        for num in nums: 
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > k:
                ans.add(num)
            if len(ans) > 1: 
                return list(ans)

        return list(ans)
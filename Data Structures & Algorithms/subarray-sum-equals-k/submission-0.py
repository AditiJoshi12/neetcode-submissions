class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = {0: 1}
        prev = 0  #previous sum
        ans = 0 #store the answer

        for num in nums:
            curr = prev + num

            if curr - k in counter:
                ans += counter[curr - k]

            counter[curr] = counter.get(curr, 0) + 1
            prev = curr
        
        return ans
        
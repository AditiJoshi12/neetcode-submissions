class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_nums = {}
        triplets = set()
        n = len(nums)

        for i, num in enumerate(nums):
            hash_nums[num] = i

        for i in range(n):
            for j in range(i+1, n):
                rem = - (nums[i]+nums[j])
                if rem in hash_nums and hash_nums[rem] != i and hash_nums[rem] != j:
                    l = [nums[i], nums[j], rem]
                    l = tuple(sorted(l))
                    triplets.add(l)

        return list(triplets)
        
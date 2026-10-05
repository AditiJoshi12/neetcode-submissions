class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}

        for i, num in enumerate(nums):
            if num in freq:
                l_j = freq.get(num, [])
                for j in l_j:
                    if abs(i - j) <= k:
                        return True
                freq[num].append(i)
            else:
                freq[num] = [i]

        return False
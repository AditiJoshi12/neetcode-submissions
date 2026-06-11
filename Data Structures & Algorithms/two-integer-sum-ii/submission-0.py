class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers)
        j = n - 1

        while i < n-1 and j > -1 and i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i = i+1
            else:
                j = j-1
        
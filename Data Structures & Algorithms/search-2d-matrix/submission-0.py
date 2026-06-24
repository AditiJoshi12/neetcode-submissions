class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatMatrix = [cell for row in matrix for cell in row]

        left = 0
        right = len(flatMatrix)-1

        while left <= right:
            mid = (left+right)//2
            if flatMatrix[mid] == target:
                return True
            elif flatMatrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])  
        left, right = 0, m*n - 1

        while left <= right:
            mid = (left+right)//2 
            row = mid //n
            col = mid%n
            midval = matrix[row][col]

            if midval == target:
                return True
            elif midval < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights)
        j = n-1
        max_area = 0

        while i<j:
            
            if heights[i] < heights[j]:
                area = heights[i]*(j-i)
                i = i+1
            else:
                area = heights[j]*(j-i)
                j = j-1
            max_area = max(area, max_area)

        return max_area

        
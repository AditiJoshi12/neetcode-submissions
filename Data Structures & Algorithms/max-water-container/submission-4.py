class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights)
        j = n-1
        max_area = 0

        while i<j:
            h_i = heights[i]
            h_j = heights[j]
            if heights[i] < heights[j]:
                area = h_i*(j-i)

                while i < j and heights[i] <= h_i:
                    i += 1

            else:
                area = h_j*(j-i)
                while i < j and heights[j] <= h_j:
                    j -= 1
            max_area = max(area, max_area)

        return max_area

        
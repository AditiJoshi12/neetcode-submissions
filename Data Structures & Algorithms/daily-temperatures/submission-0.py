class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        # we should store the index of the day with a temperature 
        # higher than the current situation 

        # we traverse the array backwards and store this value in a monotonically decreasing stack

        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result
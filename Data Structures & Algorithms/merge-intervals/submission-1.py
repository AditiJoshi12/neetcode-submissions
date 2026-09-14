class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [] 

        intervals.sort()
        results = [intervals[0]]

        i, n = 0, len(intervals)

        for i in range(1, n):
            current_interval = intervals[i]
            last_added_interval = results[-1]

            if current_interval[0] <= last_added_interval[1]: 
                last_added_interval[1] = max(last_added_interval[1], current_interval[1])
            else:
                results.append(current_interval)

        return results

        
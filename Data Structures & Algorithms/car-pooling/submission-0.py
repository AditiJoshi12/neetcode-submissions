class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta = [0]*1001

        for count, start, end in trips: 
            delta[start] += count
            delta[end] -= count 

        current_passengers = 0
        for change in delta:
            current_passengers += change
            if current_passengers > capacity:
                return False

        return True


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0 
        min_time_left = 0

        pairs = sorted(zip(position, speed), reverse=True)

        for pos, spd in pairs:
            time_left = (target-pos)/spd 

            if time_left > min_time_left:
                fleet += 1
                min_time_left = time_left

        return fleet
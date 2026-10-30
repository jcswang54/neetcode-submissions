class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)   # closest to target first
        fleets = 0
        lead_time = 0                     # arrival time of the fleet just ahead
        for p, s in cars:
            t = (target - p) / s
            if t > lead_time:             # slower than the fleet ahead: can't catch it
                fleets += 1
                lead_time = t             # this car leads a new fleet
            # else: it catches up and joins; the fleet's time stays lead_time
        return fleets

        """we compare the time a car takes with the time the car ahead takes to decide whether to update the lead_time and fleet numbers or not"""
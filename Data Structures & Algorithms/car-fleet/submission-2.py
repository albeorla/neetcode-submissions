class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        fleets = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:

            solo_time = (target - pos) / spd
        
            if not fleets or solo_time > fleets[-1]:
                fleets.append(solo_time)
    
        return len(fleets)
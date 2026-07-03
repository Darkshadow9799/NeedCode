class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i])
        fleet_count = 0
        prev_fleet = 0
        for index in sorted_indices[::-1]:
            arrival_ = (target - position[index]) / speed[index]
            if arrival_ > prev_fleet:
                fleet_count += 1
                prev_fleet = arrival_
        
        return fleet_count
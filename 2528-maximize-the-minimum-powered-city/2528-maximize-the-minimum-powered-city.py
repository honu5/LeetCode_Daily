class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def can_achieve_min_power(target_min_power: int, available_stations: int) -> bool:
           
            power_additions = [0] * (num_cities + 1)
            current_added_power = 0
          
            for city_idx in range(num_cities):
                current_added_power += power_additions[city_idx]
              
                current_city_power = initial_power[city_idx] + current_added_power
                power_deficit = target_min_power - current_city_power
              
                if power_deficit > 0:
                    # Check if we have enough stations to cover the deficit
                    if available_stations < power_deficit:
                        return False
                  
                    available_stations -= power_deficit
                  
                    rightmost_position = min(city_idx + r, num_cities - 1)
                  
                    affected_start = max(0, rightmost_position - r)
                    affected_end = min(rightmost_position + r, num_cities - 1)
                  
                    power_additions[affected_start] += power_deficit
                    power_additions[affected_end + 1] -= power_deficit
                  
                    current_added_power += power_deficit
          
            return True
      
        num_cities = len(stations)
      
        power_diff = [0] * (num_cities + 1)
      
        for station_idx, station_power in enumerate(stations):
            left_bound = max(0, station_idx - r)
            right_bound = min(station_idx + r, num_cities - 1)
          
            # Update difference array
            power_diff[left_bound] += station_power
            power_diff[right_bound + 1] -= station_power
      
        initial_power = list(accumulate(power_diff))
      
        left, right = 0, 1 << 40  
        while left < right:
            mid = (left + right + 1) >> 1
          
            if can_achieve_min_power(mid, k):
                left = mid
            else:
                right = mid - 1
      
        return left

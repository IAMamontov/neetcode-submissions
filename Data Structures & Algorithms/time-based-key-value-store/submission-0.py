from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.time_map_dict[key]
        result = ""
        left = 0
        right = len(values_list) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values_list[mid][0] <= timestamp:
                result = values_list[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
        

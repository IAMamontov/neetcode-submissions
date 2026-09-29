class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        leaders = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        for i in range(len(cars)):
            time = int((target - cars[i][0]) / cars[i][1])
            if len(leaders) == 0 or time > leaders[-1]:
                leaders.append(time)
        return len(leaders)
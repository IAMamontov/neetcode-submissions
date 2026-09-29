class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        leaders = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            if len(leaders) == 0 or time > leaders[-1]:
                leaders.append(time)
        return len(leaders)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_numbers_map = {}
        for current_index in range(len(nums)):
            difference = target - nums[current_index]
            if difference in visited_numbers_map:
                return [visited_numbers_map[difference], current_index]
            visited_numbers_map[nums[current_index]] = current_index

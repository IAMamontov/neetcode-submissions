class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates_dict = {}
        for i in range(len(nums)):
            addition = target - nums[i]
            if addition in candidates_dict:
                return [candidates_dict[addition], i]
            else:
                candidates_dict[nums[i]] = i
        

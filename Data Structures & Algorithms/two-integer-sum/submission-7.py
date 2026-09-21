class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        additions_dict = {}
        for i in range(len(nums)):
            addition = target - nums[i]
            if addition in additions_dict:
                return [additions_dict[addition], nums.index(addition, i)]
            if addition in nums[i:]:
                additions_dict[addition] = nums.index(addition)
        print(additions_dict)
        for i in range(len(nums)):
            if target - nums[i] in additions_dict and target - nums[i] !=  nums[i]:
                return [i, additions_dict[target - nums[i]]]
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        additions_dict = {}
        for i in range(len(nums)):
            addition = target - nums[i]
            if addition in nums:
                if addition == nums[i]:
                    additions_dict[addition] = nums.index(addition, i)
                additions_dict[addition] = nums.index(addition)
        print(additions_dict)
        for i in range(len(nums)):
            if target - nums[i] in additions_dict:
                return [i, additions_dict[target - nums[i]]]
        
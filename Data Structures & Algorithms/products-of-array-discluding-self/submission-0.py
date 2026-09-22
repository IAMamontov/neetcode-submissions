class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ar = []
        prefix = []
        suffix = []
        prefix.append(1)
        suffix.append(1)
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
            suffix.append(suffix[i - 1] * nums[len(nums) - i])
        for i in range(len(nums)):
            ar.append(prefix[i] * suffix[len(nums) - i - 1])
        return ar


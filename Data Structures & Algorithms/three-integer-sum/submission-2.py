class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left_pointer = i + 1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if current_sum < 0:
                    left_pointer += 1
                elif current_sum > 0:
                    right_pointer -= 1
                elif current_sum == 0:
                    result_list.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
        return result_list
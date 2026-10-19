class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_left = height[left_pointer]
        max_right = height[right_pointer]
        total_water = 0
        while left_pointer < right_pointer:
            if max_left < max_right:
                total_water += max_left - height[left_pointer]
                left_pointer += 1
                max_left = max(max_left, height[left_pointer])
            else:
                total_water += max_right - height[right_pointer]
                right_pointer -= 1
                max_right = max(max_right, height[right_pointer])
        return total_water

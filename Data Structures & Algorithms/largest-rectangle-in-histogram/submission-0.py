class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights_stack = []
        for current_index,  current_height in enumerate(heights):
            start_index = current_index
            while heights_stack and current_height < heights_stack[-1][1]:
                popped_index, popped_height = heights_stack.pop()
                current_area = popped_height * (current_index - popped_index)
                max_area = max(current_area, max_area)
                start_index = popped_index
            heights_stack.append((start_index, current_height))
        for start_index, remaining_height in heights_stack:
            final_area = remaining_height * (len(heights) - start_index)
            max_area = max(final_area, max_area)
        return max_area

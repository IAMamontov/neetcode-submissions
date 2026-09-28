class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        decrease_temp_indices = []
        for current_index, current_temp in enumerate(temperatures):
            while len(decrease_temp_indices) > 0 and temperatures[current_index] > temperatures[decrease_temp_indices[-1]]:
                current_from_stack = decrease_temp_indices.pop()
                result[current_from_stack] = current_index - current_from_stack
            decrease_temp_indices.append(current_index)
        return result


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_start_candidates = []
        for num in nums_set:
            if num - 1 not in nums_set:
                seq_start_candidates.append(num)
        seq_counter = 1
        max_seq_len = 0
        for candidate in seq_start_candidates:
            while candidate + 1 in nums_set:
                seq_counter += 1
                candidate += 1
            if seq_counter > max_seq_len:
                max_seq_len = seq_counter
            seq_counter = 1
        return max_seq_len
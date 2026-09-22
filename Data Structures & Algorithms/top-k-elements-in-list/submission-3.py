from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counter_nums:
            buckets[counter_nums[num]].append(num)
        result_list = []
        for num_list in reversed(buckets):
            if num_list != []:
                for num in num_list:
                    result_list.append(num)
                    k -= 1
                    if k == 0:
                        return result_list
        return result_list

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums).most_common()
        return list(dict(counter_nums).keys())[:k]

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid_k = left + (right - left) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid_k - 1) // mid_k
            if total_hours <= h:
                min_k = mid_k
                right = mid_k - 1
            else:
                left = mid_k + 1
        return min_k
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1
        max_margin = 0
        while sell_day < len(prices):
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
            current_margin = prices[sell_day] - prices[buy_day]
            max_margin = max(current_margin, max_margin)
            sell_day += 1
            
        return max_margin


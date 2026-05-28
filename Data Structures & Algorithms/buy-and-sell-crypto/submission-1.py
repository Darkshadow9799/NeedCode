class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buying_price)
            if (min_buying_price > prices[i]): min_buying_price = prices[i]
        return max_profit
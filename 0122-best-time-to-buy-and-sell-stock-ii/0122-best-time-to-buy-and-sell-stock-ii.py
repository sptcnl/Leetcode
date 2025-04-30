class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i]- buy > 0:
                total += prices[i] - buy
                buy = prices[i]
            else:
                buy = min(buy, prices[i])
        return total
                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                Curprofit = prices[r] - prices[l]
                maxProfit = max(maxProfit,Curprofit)
        return maxProfit
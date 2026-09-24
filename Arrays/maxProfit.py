class Solution:
    def maxProfit(self, prices):
        mini = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])
        return maxProfit
obj = Solution()
prices = [7,1,5,3,6,4]  
print(obj.maxProfit(prices))  
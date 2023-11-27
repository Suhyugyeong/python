class Solution:
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = sell - buy
                if profit > result:
                    result = profit
        return result
    
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result) # 5
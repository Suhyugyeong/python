class Solution:
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        min_price = prices[0]
        for _, now_price in enumerate(prices):
        # 반복문을 돌려!
            min_price = min(min_price, now_price)
            # 최소금액을 구한다. 최소금액 = min(현재금액, 최소금액)
            profit = now_price - min_price
            # 수익 = 현재금액-최소금액
            result = max(profit, result)
            # result = max(수익, result)
        return result
    
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result) # 5
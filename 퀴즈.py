class Solution:
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            result = max(prices[i], min_price, result)
    
            
        #현재 최소금액 구한다. 맨앞에꺼 7
        #반복문 돌려, 최소금액 구한다. 최소금액 = (현재 금액, 최소금액
        # 수익 = 현재금액 - 최소금액
        #result는 = max (수익, result)
        return result
    
sol= Solution()
prices = [7,1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result) #5
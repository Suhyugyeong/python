class Solution:
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        #최대 이익 저장, 초기값 설정
        min_price = prices[0]
        #현재까지의 최소 주가, 초기값은 리스트의 첫번째 주가
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            result = max(prices[i], min_price, result)
            #현재 날짜의 주가, 현재까지의 최소 주가, 현재까지의 최대 이익 중 max
            #현재까지의 최대 이익을 업데이트
    
            
        #현재 최소금액 구한다. 맨앞에꺼 7
        #반복문 돌려, 최소금액 구한다. 최소금액 = (현재 금액, 최소금액
        # 수익 = 현재금액 - 최소금액
        #result는 = max (수익, result)
        return result
    
sol= Solution()
#Solution의 인스턴스
prices = [7,1, 5, 3, 6, 4]
result = sol.max_profit(prices)
#sol인스턴스의 max_profit은 위에서 정의한 메서드
print(result) #5
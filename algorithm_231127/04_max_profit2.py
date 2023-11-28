#주식거래에서 얻을 수 있는 최대 이익을 계산하는 Greedy 알고리즘
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        result = 0
        min_price = prices[0]
        for _, now_price in enumerate(prices):
        #enumerate : 순회 가능한 객체를 순회하면서 동시에 각 원소의 인덱스에 접근할 수 있다
        #enumerate 함수는 각 순회 단계에서 (인덱스, 값)의 튜플을 반환하는데
        #여기서 _는 인덱스를 무시하고 값만 사용하겠다는 의미
        # 주식 가격 리스트를 순회하면서 각 날짜의 주식 가격을 now_price에 할당
            min_price = min(min_price, now_price)
            # 현재 날짜의 주식 가격과 이전까지의 최소 가격 중 작은 값을 선택하여 최소 가격을 갱신
            profit = now_price - min_price
            # 현재 날짜에서 주식을 팔았을 때 얻는 이익을 계산
            result = max(profit, result)
            # 현재까지의 최대 이익과 현재 날짜에서 얻은 이익 중 큰 값을 선택하여 최대 이익을 갱신!
            #max() 함수에 하나의 인자만 전달하면 오류        
        return result
    
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result) # 5
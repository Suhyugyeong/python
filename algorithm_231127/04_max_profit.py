#브루트포스(Brute Force) 방식을 사용하여 배열에서 얻을 수 있는 최대 이익을 계산
#성능이 매우 구리다..
#두 날짜를 선택하여 각 날짜의 주식 가격을 비교, 가능한 모든 이익 중 최대 이익 찾기!
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        #타입 힌트~!
        #함수 선언 : max_profit은 클래스 Solution의 메서드
        #이 함수는 클래스 메서드이며, 클래스의 인스턴스를 나타내는 self를 매개변수로 받는다.
        #prices라는 매개변수는 리스트로 그 안의 원소는 정수이다.
        #->int: 함수가 정수를 반환한다, 는 의미
        result = 0
        #최대 이익을 계산하기 위한 초기값을 설정하는 부분
        #초기에 최대이익을 0으로 설정하여 시작한다는 의미
        #여기서 초기값을 0으로 설정하는 이유는 아직 어떤 주식도 사지 않았기 때문에..
        #현재까지의 최대이익은 0이다!! 아무것도 사고 팔지 않았으니께..
        for i in range(len(prices) - 1):
            buy = prices[i]
            #현재 날짜 i에서 주식을 사는데 필요한 비용을 나타내는 변수 buy
            for j in range(i + 1, len(prices)):
                #현재 날짜 이후의 날짜 순회하며 가능한 모든 판매 날자 확인
                sell = prices[j]
                #현재 날짜 i에서 주식을 팔 때의 가격 변수 sell
                profit = sell - buy
                if profit > result:
                    result = profit
                    #계산된 이익이 현재까지의 최대 이익(result)보다 크면 값을 업데이트
        return result
    
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result) # 5
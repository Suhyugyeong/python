import math

print(math)
#<module 'math' (built-in)>
print(type(math))
#<class 'module'>

print(math.pi)
print(math.sqrt(9)) #3.0
#제곱근을 계산하기 위한 함수
#반환값은 부동소수점 숫자

# 원의 둘레 공식 = pi * 반지름 * 2
# 원의 넓이 공식 = pi * 반지름 ** 2
area = 78.53981633974483
print(f"반지름은 {math.sqrt(area/(math.pi))}")
#반지름은 루트 파이 분의 원의 넓이
from math import pi, sqrt

print(pi)
print(sqrt(9))

# 원의 둘레 공식 = pi * 반지름 * 2
# 원의 넓이 공식 = pi * 반지름 ** 2

area = 78.53981633974483
print(f"반지름은 {sqrt(area/(pi))}")
#앞에는 import math만 했을 때, math. 이런 식으로..
#여기서는 from math import pi, sqrt를 명시함으로써, 앞에 math.를 생략 가능한..!
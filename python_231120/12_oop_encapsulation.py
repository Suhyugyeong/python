#만들어둔 shape 모듈을 사용하여 사각형의 둘레 구하기

import module.shape as s

rectangle1 = s.Rectangle(3, 2)
rectangle2 = s.Rectangle(4, 6)
print(rectangle1.get_perimeter())
print(rectangle2.get_perimeter())
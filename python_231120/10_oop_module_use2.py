# from module import rrn
# data = "931120-1234567"
# print(rrn.birth(data))
#(1993, 11, 20)

import module.rrn as r
#r이라는 별칭으로 가져와서 사용한다..
#모듈이름이 길거나 여러 번 사용해야할 때 코드를 간단하게 하기 위해 사용한다..
data = "931120-1234567"
print(r.birth(data))
#(1993, 11, 20)

# from module.rrn import birth
# data = "931120-1234567"
# print(birth(data))
#(1993, 11, 20)
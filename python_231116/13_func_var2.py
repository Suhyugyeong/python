def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

# calc_list = [plus, minus]
# print(calc_list[0](5, 6))
# print(calc_list[1](17, 1))

calc_dict = {'더하기' : plus, '빼기' : minus}
print(calc_dict['더하기'](10, 10))
print(calc_dict['빼기'](43, 20))
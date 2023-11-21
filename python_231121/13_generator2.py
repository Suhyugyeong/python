#range함수가 대표적으로 제너레이터다....

def get_many_type_data():
    while True:
        yield 1
        yield '문자열'
        yield True

type_generator = get_many_type_data()

for i in range(5):
    print(next(type_generator))
    
#1
#문자열
#True
#1
#문자열
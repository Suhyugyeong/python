print(dir(object)) # object 클래스가 가진 속성들

class Car:
    pass

# 클래스를 생성하면 object가 가진 속성들을 물려받고, 3개의 속성은 자동으로 추가된다.
# {'__module__', '__dict__', '__weakref__'}
print(set(dir(Car)) - set(dir(object)))
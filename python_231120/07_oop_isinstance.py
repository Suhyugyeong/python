# isinstance는 객체가 어떤 클래스의 인스턴스인지 알려주는 함수
#객체가 특정 클래스의 인스턴스인지 여부를 확인하는데 사용 True, False
class Car:
    def __init__(self, id):
        self.id = id

c = Car('123가5678')
print(isinstance(c, Car))
#c는 확인하려는 객체, Car는 확인하려는 클래스 또는 튜플
print(isinstance(c, object))

print(isinstance('abc', str))
print(isinstance(123, int))
print(isinstance(True, int))
print(isinstance(True, bool))

print(isinstance('abc', object))
print(isinstance(123, object))
print(isinstance(True, object))

print(isinstance(Car, object))
print(isinstance(str, object))
print(isinstance(int, object))
print(isinstance(bool, object))

#결론은 어쨌든 다 True임...
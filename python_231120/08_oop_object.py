print(dir(object)) 
#['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# dir는 객체의 속성이나 메서드를 나열한다.
# object 클래스는 파이썬에서 모든 클래스의 기본 부모 클래스이기 때문에, 이 속성은 모든 클래스에 공통적으로 포함..

class Car:
    #Car라는 이름의 클래스를 정의하겠다..
    pass
#그러나 어떤 속성도 메서드도 정의되어 있지 않으니, 최소 pass로 내용이 비어있음을 나타낸다.
#문법적 요구를 만족시키기 위해 사용하는 더미 동작!!


print(set(dir(Car)) - set(dir(object)))
#set은 내장된 데이터 타입 중 하나로, 중복되지 않은 항목들로 구성된 변경 가능한 컬렉션을 나타냄
#set은 중복값을 허용하지 않고, 순서가 없는 자료 구조다.
#이 식으로 car 클래스에만 있는 속성들의 집합을 나타냄
#{'__dict__', '__weakref__', '__module__'} => object 클래스에서 상속받은 속성이 아니라 car 클래스에만 있는 속성

# print(dir(Car))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']        
class Animal:
    # 생성자(__init__) : 객체를 생성할 때, 가장 먼저! 호출되는 함수
    # 즉, 객체를 생성하면 __init__함수가 자동으로 실행되어, 생성된다.
    def __init__(self):
        self.name = 'unnamed'
        self.age = -1
    # 클래스 함수
    def info(self):
        print(f"안녕하세요! 저는 {self.name}입니다. {self.age}살이에요")

pig = Animal()
pig.name = '꿀꿀이'
pig.age = 2
pig.info()

panda = Animal()
panda.info()
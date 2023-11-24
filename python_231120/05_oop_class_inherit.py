#클래스와 상속을 사용하여 객체 지향 프로그래밍을 구현한 예시
#상속은 부모 클래스의 특성을 자식 클래스에게 물려주는 것
#오버라이딩은 자식 클래스에서 부모 클래스의 메서드를 재정의하여 새로운 동작을 제공하는 것입니다.
class Animal:
    def __init__(self):
        self.name = 'unnamed'
        self.age = -1
    def info(self):
        print(f"정보! 이름은 {self.name}, 나이는 {self.age}살")
        
class Human(Animal):
    def __init__(self):
        self.name = "홍길동"
        self.age = 1
        self.job = "학생"
        super().__init__() 
        #super() 부모 클래스의 메서드를 호출
        #Human 클래스의 생성자에서 부모 클래스인 Animal클래스 생성자를 호출
        #Human 클래스는 Animal 클래스를 상속받았고, Human 클래스의 객체가 생성될 때, Animal 클래스의 초기화 작업이 필요
        #굳이 __init__를 하는 이유는 Human 클래스의 인스턴스가 생성될 때 Animal 클래스의 초기화도 함께 이루어지게 하기 위해..
        #self.name, self.age, 그리고 self.job을 초기화합니다. super().__init__()를 호출하면 Animal 클래스에서 정의된 self.name과 self.age가 초기화되며, 
        #그 후에 Human 클래스에서 추가로 필요한 속성인 self.job을 초기화할 수 있습니다.
        #즉, 부모 클래스의 변경이 자식 클래스에 영향을 미치지 않도록 하는 객체 지향 프로그래밍의 기본 원칙 중 하나인 '캡슐화'와 '다형성'을 지원하는 메커니즘 중 하나
        
    def speak(self, data):
        print(f"{self.name} : {data}")
    def info(self): 
        # 자식클래스에서 재정의해서 사용 : 오버라이딩(Overriding)
        #여기서 Animal 클래스에는 info 메서드가 있고
        #Human 클래스에서는 이 메서드를 다시 정의하여 자식 클래스에 특화된 동작을 수행합니다. 
        print(f"{self.name} : 안녕하세요. 제 소개를 드립니다. 이름은 {self.name}이고, 나이는 {self.age}살이에요. 직업은요, {self.job}(이)에요")


hong = Human()
hong.name = '김길동'
hong.age = 20
hong.info()
hong.speak("안녕하세요. 만나서 반가워요")

# hong = Animal()
# hong.name = '김길동'
# hong.age = 20
# hong.info()
# hong.speak("안녕하세요. 만나서 반가워요")
#Animal일 때 name, age, info() 작동 잘 하고 speak의 경우, 자식에게만 있는 메서드기 때문에 오류!
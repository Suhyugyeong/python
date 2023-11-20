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
        super().__init__() # 반드시 부모 생성자를 호출! 필수!!!
    def speak(self, data):
        print(f"{self.name} : {data}")
    def info(self): # 자식클래스에서 재정의해서 사용 : 오버라이딩(Overriding)
        print(f"{self.name} : 안녕하세요. 제 소개를 드립니다. 이름은 {self.name}이고, 나이는 {self.age}살이에요. 직업은요, {self.job}(이)에요")

hong = Human()
hong.name = '김길동'
hong.age = 20
hong.info()
hong.speak("안녕하세요. 만나서 반가워요")
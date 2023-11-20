class Animal:
    # 클래스 변수
    age = 1
    name = 'unnamed'
    # 클래스 함수
    def set_name(self, data):
        self.name = data
    # 생성자
    # 인스턴스 함수

pig = Animal()
print(pig)
print(type(pig))
print(f"우리 돼지의 이름은 {pig.name}이고, 나이는 {pig.age}살입니다.")
pig.set_name("꿀꿀이") # Animal.set_name(pig, "꿀꿀이")
print(f"우리 돼지의 이름은 {pig.name}이고, 나이는 {pig.age}살입니다.")
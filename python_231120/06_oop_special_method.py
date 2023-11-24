#특별 메서드를 사용 (__init__, __len__, __str__)
class Car:
    def __init__(self, id):
        self.id = id
        #객체 초기화 생성자 메서드
        #id라는 속성을 가지고 있다.
    def __len__(self):
        return len(self.id)
    #길이 반환 메서드
    def __str__(self):
        return "차 번호 : " + self.id
    #문자열 표현 메서드

def main():
    c = Car('123가5678')
    #Car 클래스의 객체 c를 생성하고, 생성자에 '123가5678'을 전달하여 초기화
    print(len(c))
    print(str(c))
    
main()
#여기서 함수를 호출!! 해서 위의 내용을 print할 수 있는거임..
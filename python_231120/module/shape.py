# 직사각형 : 가로의 길이, 세로의 길이가 같다.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimeter(self):
        #둘레 반환
        return 2 * (self.__get_width_plus_height__())
    def __get_width_plus_height__(self): 
        return self.width + self.height
       
       
# private method 클래스 외부에서 직접 호출되지 않도록 이름 앞에 __ 붙음..
# 직사각형 : 가로의 길이, 세로의 길이가 같다.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimeter(self):
        return 2 * (self.__get_width_plus_height__())
    def __get_width_plus_height__(self): # private method
        return self.width + self.height
#리스트 컴프리헨션은 일반적으로 for문 뒤에 if문이 나온다.
#리스트를 간결하게 만들기 위한 표현 방법 중 하나입니다. 
#리스트 컴프리헨션은 반복문과 조건문을 사용하여 리스트를 생성하는 간편한 방법을 제공합니다.
names = ["허준", "강민서", "강은영", "권보경", "박종섭", "박준영", "서유경", "신혜인", "유재인", "이지은", "정준혁", "천다영", "최아별", "최지성"]

# gangs = [i for i in names if i[0] == "강"]
choi_gangs = [i for i in names if i[0] == "강" or i[0] == "최"]
print(choi_gangs)
single_names = [i for i in names if len(i) <=2 ]
print(single_names)

#even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
#[4, 16, 36, 64, 100]

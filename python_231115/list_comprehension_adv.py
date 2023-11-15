names = ["허준", "강민서", "강은영", "권보경", "박종섭", "박준영", "서유경", "신혜인", "유재인", "이지은", "정준혁", "천다영", "최아별", "최지성"]

gangs = [i for i in names if i[0] == "강"]
choi_gangs = [i for i in names if i[0] == "강" or i[0] == "최"]
print(choi_gangs)
single_names = [i for i in names if len(i) <=2 ]
print(single_names)
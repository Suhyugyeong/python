hong_info = ['홍길동', 20]
name, age = hong_info
print(name, age)

eight_divisor = [1, 2, 4, 8]
odd, *even = eight_divisor
print(odd, even)

yoo_info = ['유재석', 'TMI1', 30, 'TMI2', '서울 강남구']
name, _, age, _, address = yoo_info
print(name, age, address)

park_info = ['박서준', 'TMI1', 'TMI2', 'TMI3', '더 마블스'] # open_chat과 연계해서 공부하기!
name, *_, works = park_info
print(name, works)
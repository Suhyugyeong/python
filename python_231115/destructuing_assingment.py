my_list = ["유", 21]
name, age = my_list
print(name, age)

eight_divisor = [1,2,4,8]
odd, *even = eight_divisor
# 별을 붙였을 때 list로 반환한다는 사실이 중요함!!
print(odd, even)

kouhei_info = ["matsuda", "tmi1", 36, "tmi2", "도쿄"]
name, _, age, _, address =  kouhei_info
print(_)
print(name, age, address)
#tmi2를 반환함

park_info = ["박명수", "tmi:쇠독있음", "tmi:딸있음.", "tmi:박탈성구순염앓음", "무한도전"]
name, *_, works = park_info
print(name, works)
print(_)
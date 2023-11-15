my_list = ["유", 21]
name, age = my_list
print(name, age)

eight_divisor = [1,2,4,8]
odd, *even = eight_divisor
print(odd, even)
#파이썬에서 사용되는 언패킹 기능 중 하나
#리스트나 튜플과 같은 iterable 데이터를 각 변수에 나누어 저장
# 왼쪽부터 순서대로 뽑고, 별은 나머지 모두를 의미하고 list로 반환한다.
# odd, two, *even = eight_divisor
# print(odd, two, even)

kouhei_info = ["matsuda", "kasyu", 36, "haiyuu", "도쿄"]
name, _, age, _, address =  kouhei_info
print(_)
#_는 언패킹할 때 사용됨
#사용하지 않을 변수의 이름으로 언더스코어를 자주 사용
#사용하지 않는 변수이기 때문에 프린트 하면 제일 마지막으로 할당된 값(haiyuu)으로 유지
print(name, age)

park_info = ["박명수", "tmi:쇠독있음", "tmi:일렉트로닉음악좋아함", "tmi:박탈성구순염앓음", "무한도전"]
name, *_, works = park_info
print(name, works)
print(_)
#여기서 언더스코어 처리한 게 다 나오는 이유는 위에서 나머지를 다 _ 하나로 묶어버렸기 때문에
#그리고 이게 가능한 건 리스트 안에서 연달아서 있어서 묶을 수 있기 때문.. 
pl = []

#끝에 요소를 추가
pl.append("수능")
pl.append("첫눈")

#원하는 위치에 요소를 삽입
pl.insert(2,"서브웨이")
print(pl)

#꺼내기
# pl.pop()
# print(pl)
print(pl.pop())
#반환값이 있다는 것 , 커서 올려보면 -> any

print(pl.pop(1))
print(pl)

print("첫눈" in pl)

#in으로 요소 존재여부 반환(응용)
# if 1115 in pl :
#     pass
# else :
#     pl.append(1115)
    
if 1115 not in pl :
    pl.append("수요일")
print(pl)

#리스트 정렬하기
pl.sort()
print(pl)

#리스트 뒤집기

pl.reverse()
print(pl)

special_lec = ["git", "uxui", "취업특강", "포트폴리오"]
pl.extend(special_lec)
print(pl)

#위치 반환(동일한 요소가 중복된 경우, 앞에 있는 인덱스를 반환/ 리스트에 없으면 오류 ->이럴 땐 if문으로 사용)
print(pl.index("포트폴리오"))

#같은 값 개수 세기 "수능"이 리스트에 하나 있음..
print(pl.count("수능"))
print(pl)

#요소의 개수 총 7개 요소가 있다..
print(len(pl))

#리스트 반복
for i in pl:
    print(i)
    
for i in range(len(pl)):    
    print(i)
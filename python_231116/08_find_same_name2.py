names = input().split()
#정형돈 정준하 유재석 박명수 박명수

names_dict = {}
names_set = set()

for i in names:
    if i in names_dict:
        names_dict[i] += 1
        names_set.add(i)
    else:
        names_dict[i] = 1

print(names_dict)
#{'정형돈':1, '정준하':1, '유제석':1, '박명수':2}
print(names_set)
#{'박명수}

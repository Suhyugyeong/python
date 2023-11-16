names = input().split()

# names_dict = {i : names_dict.get(i,0) + 1 for i in names}
names_dict = {}
# 1. names를 반복해서 names_dict를 채워나간다.
# 1-1. names_dict에 이름이 있으면 +1, 없으면 1
for i in names:
    if i in names_dict:
        names_dict[i] += 1
    else:
        names_dict[i] = 1

names_set = set()
# 2. names_dict를 반복해서 key, value를 가지고
# 2-1. value가 2 이상이면 names_set에 추가
for k, v in names_dict.items():
    if v >= 2:
        names_set.add(k)

# 3. names_set 출력
print(names_set)
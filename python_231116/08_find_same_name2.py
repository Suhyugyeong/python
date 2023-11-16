names = input().split()

names_dict = {}
names_set = set()

for i in names:
    if i in names_dict:
        names_dict[i] += 1
        names_set.add(i)
    else:
        names_dict[i] = 1

print(names_dict)
print(names_set)
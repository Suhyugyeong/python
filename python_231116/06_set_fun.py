num_set1 = set ([1,2,3])
num_set2 = set ([3,4])

num_set2.add(5) #set2!!에 요소추가
num_set1.update(num_set2) #세트에 다른 세트를 추가(합집합)

print(num_set1)

print(num_set2.pop())
num_set2.remove(5) #5를 삭제해주고
print(num_set2)
num_set2.clear()
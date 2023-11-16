my_set1 = set([1,2,3,4,5,6])
my_set2 = set([4,5,6,7,8,9])

# 합집합
print(my_set1 | my_set2)
print(my_set1.union(my_set2))
# my_set1.update(my_set2)
# print(my_set1)

# 교집합
print(my_set1 & my_set2)
print(my_set1.intersection(my_set2))
# my_set1.intersection_update(my_set2)
# print(my_set1)

# 차집합
print(my_set1 - my_set2)
print(my_set1.difference(my_set2))
# my_set1.difference_update(my_set2)
# print(my_set1)

# 대칭차집합
print(my_set1 ^ my_set2)
print(my_set1.symmetric_difference(my_set2))
# my_set1.symmetric_difference_update(my_set2)
# print(my_set1)
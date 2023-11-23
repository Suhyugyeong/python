import collections

student_list = []
student_dic = collections.Counter(student_list)

print(student_list)
#counter로 반환되니까
print(dict(student_list))
#로 바꿔주기

for k, v in student_list.items():
    print(k,v)

#most_common = 리스트에 튜플로 들어가면서 순서가 생긴다..
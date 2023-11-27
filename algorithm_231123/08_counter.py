import collections

student_list = ["서유경", "정준혁", "서유경", "유재현", "박종섭", "박준영", "서유경", "박준영"]
student_counter = collections.Counter(student_list)

print(student_counter)
print(student_counter.most_common())
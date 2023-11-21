import re

# c_obj = re.compile('[a-z]+')
# match_obj =  c_obj.search("파이th0n")
#밑에것처럼 간단하게 작성 가능..

match_obj = re.search('[a-z]+', '파이th0n')
#search는 문자열 전체를 확인한다..

print(match_obj) #<re.Match object; span=(2, 4), match='th'>
print(match_obj.group()) #th
print(match_obj.start()) #2
print(match_obj.end()) #4
print(match_obj.span()) #(2,4)
import re

# c_obj = re.compile('[a-z]+')
# match_obj =  c_obj.match("pyth0n")
#밑에것처럼 간단하게 작성 가능..

match_obj = re.match('[a-z]+', 'pyth0n')


print(match_obj) #<re.Match object; span=(0, 4), match='pyth'>
print(match_obj.group()) #pyth
print(match_obj.start()) #0
print(match_obj.end()) #4
print(match_obj.span()) #(0,4)
import re

match_obj = re.search('(\w+)\s+([0,1]{3}[-]\d{4}[-]\d}{4})', "홍길동 010-1234-1234")

print(match_obj)

print(match_obj.group(0)) #매칭된 문자열 전체 출력
print(match_obj.group(1)) #그룹 1 출력
print(match_obj.group(2)) #그룹 2 출력


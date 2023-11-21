import re

# re.sub(패턴, 대체문자, 대상문자)
target = 'aabbcc'
target = re.sub('[a]+',"안녕", target)

print(target)
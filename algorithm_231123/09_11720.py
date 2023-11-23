#readline은 엔터도 포함하고 있어서 여기에서 int를 해주면 오류발생하니까 rstrip()을 해줘야한다.. 

import sys
N = sys.stdin.readline()
#여기서 N변수를 쓰지 않을 거니까, 변수 선언 생략해도 됨..
nums = sys.stdin.readline().rstrip()

result = 0
for i in nums:
    result += int(i)
print(result)
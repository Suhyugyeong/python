import sys

try:
    num = int(sys.stdin.readline())
    print(100/num)
except Exception as e:
    print(f"{e.__class__} : {e}")
    
print('프로그램이 정상적으로 종료되었습니다.')
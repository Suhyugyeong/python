import sys

try:
    num = int(sys.stdin.readline())
    result = 100/num
except Exception as e:
    print(f"예외가 발생했습니다.")
else:
    # try 블록 전체가 '무사히' 실행되었을 때 실행되는 else 블록
    print(f"결과는 {result}입니다.")

print('프로그램이 정상적으로 종료되었습니다.')
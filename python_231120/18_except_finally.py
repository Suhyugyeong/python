import sys

try:
    num = int(sys.stdin.readline())
    result = 100/num
except Exception as e:
    print(f"예외가 발생했습니다.")
else:
    print(f"결과는 {result}입니다.")
finally:
    # 예외 발생 여부에 관계없이 무조건 실행!
    print('프로그램이 정상적으로 종료되었습니다.')
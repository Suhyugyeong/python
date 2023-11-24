import sys

try:
    num = int(sys.stdin.readline())
    print(100/num)
    #결과가 float number로 나옴..
    #만약 0을 넣을 경우는, ZeroDivisionError가 발생
    #sys.stdin.readline()으로 사용자로부터 입력을 받으면, 개행 문자(\n)가 문자열에 포함
    #따라서 이 문자열을 정수로 변환하면 개행 문자까지 변환되어 정수가 아닌 부동 소수점 수(float)로 처리
    #개행 문자를 제거하려면 strip() 메서드를 사용하여 문자열의 양쪽 끝에서 공백 및 개행 문자를 제거할 수 있다.
    #예 num = int(sys.stdin.readline().strip())
except Exception as e:
    #예외 처리 구문으로, 예외가 발생하면 해당 예외를 e라는 이름의 변수로 받아옴
    #Exception은 모든 예외의 기본 클래스이므로 모든 예외를 처리할 수 있음
    print(f"{e.__class__} : {e}")
    #발생한 예외의 클래스와 메시지를 출력 <class 'ZeroDivisionError'> : division by zero
    
print('프로그램이 정상적으로 종료되었습니다.')
#제대로 작동했을때
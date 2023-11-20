#재귀함수를 사용하여 1부터 주어진 숫자까지의 합을 계산
def recursion_sum(num):
    # 파이썬에서함수의 매개변수로 전달되는 값은 동적타이핑을 지원
    #변수나 매개변수의 데이터 타입을 명시적으로 선언하지 않아도 된다
    
    if num == 1:
        return 1
    #종료조건 : num이 1 이면 1 반환
    result = recursion_sum(num - 1)
    return num + result

print(recursion_sum(5))


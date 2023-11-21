def find_my_num(list, value):
    """리스트 내에서 value 값에 해당하는 위치를 반환한다.
    Args:
        list (list): 숫자로 구성된 목록
        value (int): 찾으려는 숫자
    """
    #함수에 대한 간단한 도움말 문자열(docstring)
    #이 부분은 함수의 기능과 사용법을 설명하는 역할을 합니다.
    for i in range(len(list)):
        if value == list[i]: #list[i]는 list의 i번째에 있는 해당 요소
            return i
    return -1
    
print(find_my_num([1,2,3,4],3))
#[1,2,3,4]에서 3의 위치를 찾는다 = 2 

#들여쓰기 주의!!!
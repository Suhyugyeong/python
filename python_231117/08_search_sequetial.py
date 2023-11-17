def find_my_num(list, value):
    """리스트 내에서 value 값에 해당하는 위치를 반환한다.

    Args:
        list (list): 숫자로 구성된 목록
        value (int): 찾으려는 숫자
        
    """
    
    for i in range(len(list)):
        if value == list[i]:
            return i
        return -1
    
    print(find_my_num([1,2,3,4],3))
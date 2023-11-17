# 순차탐색을 통한 모든 위치 반환
import sys

#순차 탐색을 하기위한 find_my_num 생성
#중복된 요소가 있는지 확인.
def find_my_num(list, value) :
    """list 내에서 value값에 해당하는 위치 반환. (순차탐색, 선형탐색)

    Args:
        list (list): 숫자로 구성된 목록
        value (int): 찾으려는 숫자
    """
    #중복된 요소를 저장 할 비어있는 리스트 생성
    r_list = []
    for i in range(len(list)) :
        if value == list[i] :
            r_list.append(i)
    return r_list

# 숫자 요소와 찾을 숫자 요소를 입력받음.
num = [int(i) for i in sys.stdin.readline().split()]
f_num = int(sys.stdin.readline())

print(find_my_num(num, f_num))
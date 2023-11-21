#이진 탐색 알고리즘을 사용하여 정렬된 리스트에서 특정값 찾기!
def find_my_num(list, value):
    
    start, end = 0, len(list)-1
    #start =0;
    #end = len(list)-1
    while start <= end:
        #검색범위가 남아있는 동안 반복한다
        mid = (start + end) // 2
        #현재 검색 범위의 중간 인덱스를 계산
        if value < list[mid]:
            end = mid - 1
        elif value > list[mid]:
            start = mid + 1
        else:
            return mid
    return -1
    #찾고자하는 값이 없을 때는 -1

print(find_my_num([1,2,3,4,5,6,7,8], 5))
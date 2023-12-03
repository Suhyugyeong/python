#이진탐색 
def find_my_num(list, value):
    #list와 value는 함수를 호출할 때 전달되는 값을 받는 변수
    #list는 정렬된 숫자들의 리스트, value는 찾고자 하는 값
    start = 0
    end = len(list) - 1
    #현재 검색 범위의 시작과 끝
    탐색횟수 = 0
    #현재까지 이진탐색 반복 횟수
    while start <= end :
        #검색 범위가 축소될 때까지 계속
        탐색횟수 += 1
        mid = (start + end) // 2
        #현재 검색범위의 중간지점
        #//를 통해 정수 나눗셈 연산자로, 나눗셈의 결과에 소수 부분을 버림..
        if value == list[mid] : 
            print(탐색횟수)
            return mid
        elif value < list[mid]:
            end = mid - 1
            #value가 mid값보다 작으면 검색범위를 왼쪽 반으로
            #그 전 인덱스로.
        elif value > list[mid]:
            start = mid + 1
            #value가 mid값보다 크면 검색 범위를 오른쪽 반으로
            #그 다음 인덱스로..
    print(탐색횟수)
    return -1
    #만약 list에 value가 없으면 반복횟수를 출력하고 -1을 반환..

print(find_my_num([1,2,3,4,5,6,7,8], 6)) #2번만에 찾은 값5
print(find_my_num([1,2,3,4,5,6,7,8], 9)) #4번만에 찾은 값-1(리스트에 value가 없으니께..)


#-----구분선 -----
print("-----------------------------------")

def afind_my_num(alist, avalue):
    astart, aend = 0, len(alist)-1
    a탐색횟수 = 0
    while astart <= aend:
        a탐색횟수 += 1
        amid = (astart + aend) // 2
        if avalue < alist[amid]:
            aend = amid - 1
        elif avalue > alist[amid]:
            astart = amid + 1
        else:
            print(a탐색횟수)
            return amid
    print(a탐색횟수)
    return -1
print(find_my_num([1,2,3,4,5,6,7,8], 6)) #2번만에 찾은 값5
print(find_my_num([1,2,3,4,5,6,7,8], 9)) #4번만에 찾은 값-1
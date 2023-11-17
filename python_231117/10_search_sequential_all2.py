# 1. 이걸 어떻게 해야되나?  -> 순차탐색을 통한 모든 위치 반환
# 2. 일단 def를 사용하는데.... 뭘 써야되지?
def search_all(list, value):
    result = []
    for i in range(0, len(list)):
        if list[i] == value:
            result.append(i)
    return result
# 3. 입력된 값을 표기가 되야 되니 print()는 사용을 한다.
# 4. 중복의 표시..? 가 뭐더라....;; -> 리스트를 이용하면 되겠군!

nums = [int(i) for i in input().split()]
num = int(input())

print(search_all(nums, num))
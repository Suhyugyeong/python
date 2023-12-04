#퀵 정렬(Quick Sort)알고리즘을 사용해 주어진 log 리스트를 도시 이름을 기준으로 오름차순으로 정렬하는 함수

log = [['서울', '09:00:00'],
['대전', '09:00:03'],
['대구', '09:00:13'],
['서울', '09:00:59'],
['대구', '09:01:10'],
['서울', '09:03:13'],
['부산', '09:10:11'],
['부산', '09:10:25'],
['대전', '09:14:25'],
['서울', '09:19:32'],
['서울', '09:19:46'],
['서울', '09:21:05'],
['부산', '09:22:43'],
['부산', '09:22:54'],
['서울', '09:25:52'],
['서울', '09:35:21'],
['부산', '09:36:14'],
['대전', '09:37:44']]

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    left = start + 1
    right = end
    #left는 피벗 다음 요소, right는 리스트의 끝
    
    #while문을 통해 파티션을 진행 => left는 피벗보다 큰 값을 찾을 때까지 이동
    #right는 피벗보다 작은 값을 찾을 때까지 이동
    while left <= right: #1번-1번
        while left <= end and arr[left][0] <= arr[start][0]:
            left += 1
        while right > start and arr[right][0] >= arr[start][0]:
            right -= 1
            
        if left > right: #1번-2번
            #만약 left가 right보다 크면 피벗과 arr[right]를 교환
            arr[start], arr[right] = arr[right], arr[start]
        else: #1번-3번
            arr[left], arr[right] = arr[right], arr[left]
            #그렇지 않으면 arr[left]와 arr[right]를 교환
    #재귀적으로 정렬
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

from pprint import pprint
quick_sort(log, 0, len(log) - 1)
pprint(log)
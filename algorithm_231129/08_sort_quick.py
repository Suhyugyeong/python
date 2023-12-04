#퀵 정렬(Quick Sort)알고리즘 구현
#분할정복 알고리즘으로 주어진 배열 기준 원소를 기준으로 두 개의 부분 배열로 나누어 정렬하는 방식

arr = [10, 12, 17, 25, 55, 22, 35, 73, 99, 48, 5, 7]

def quick_sort(arr, start, end): #start, end는 인덱스
    if start >= end: #배열의 크기가 1이하인 경우(더 이상 나눌 수 없을 때) 함수를 종료하고 배열을 반환
        return arr
    left = start + 1 #왼쪽 포인터를 start+1으로 초기화해서 start(첫번째 원소인 피벗)랑 비교할 거임..
    right = end
    while left <= right: #왼쪽 포인터가 오른쪽 포인터보다 작거나 같은 동안 반복
        while left <= end and arr[left] <= arr[start]:
            left += 1
            #왼쪽 포인터를 오른쪽으로 이동하며, 기준 원소보다 작거나 같은 값을 찾습니다.
        while right > start and arr[right] >= arr[start]:
            right -= 1
            #오른쪽 포인터를 왼쪽으로 이동하며, 기준 원소보다 크거나 같은 값을 찾습니다.
        if left > right:
            arr[start], arr[right] = arr[right], arr[start]
            #왼쪽 포인터가 오른쪽 포인터보다 더 오른쪽에 있다면, 
            #기준 원소(arr[start])와 오른쪽 포인터가 가리키는 값(arr[right])을 교환합니다. 
            #이 때, 오른쪽 포인터가 가리키는 위치가 기준 원소의 최종 위치가 됩니다.
        else:
            arr[left], arr[right] = arr[right], arr[left]
            #그렇지 않으면, 왼쪽 포인터가 가리키는 값과 오른쪽 포인터가 가리키는 값을 교환합니다.
    quick_sort(arr, start, right - 1)
    #기준 원소를 기준으로 왼쪽 부분 배열에 대해 재귀적으로 퀵 정렬을 수행합니다.
    quick_sort(arr, right + 1, end)
    #기준 원소를 기준으로 오른쪽 부분 배열에 대해 재귀적으로 퀵 정렬을 수행합니다.

quick_sort(arr, 0, len(arr) - 1)
#초기 호출로 전체 배열에 대해 퀵 정렬을 수행합니다.
print(arr) #[5, 7, 10, 12, 17, 22, 25, 35, 48, 55, 73, 99]
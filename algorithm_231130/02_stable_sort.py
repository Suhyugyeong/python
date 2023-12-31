#병합정렬(Merge Sort)를 이용하여 주어진 log의 리스트를 정렬

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

def merge_sorted(list) :
    length = len(list)
    if length <= 1 :
        return
    mid = length // 2
    group1, group2 = list[:mid], list[mid:]
    merge_sorted(group1)
    merge_sorted(group2)
    
    idx, idx1, idx2 = 0, 0, 0
    #idx1은 group1의 현재 비교 중인 요소의 인덱스,
    #idx는 원본 리스트의 인덱스
    
    #두 그룹을 합치는 병합 단계 => 첫번째 요소인 도시이름을 비교하여 더 작은 값을 가진 요소를 원본 리스트에 병합
    while idx1 < len(group1) and idx2 < len(group2):
        #어느 한 그룹이 비교할 요소가 남아있을 때까지 반복하겠다..
        if group1[idx1][0] > group2[idx2][0]: #도시이름
            list[idx] = group2[idx2] #현재비교중인 두 도시 이름 중 작은 것을 가진 그룹의 요소를 원본 리스트에 추가
            idx2 += 1
            idx += 1
        else:
            list[idx] = group1[idx1]
            idx1 += 1
            idx += 1
    #두 그룹 중 하나에 남아있는 요소를 원본 리스트에 추가하는 과정
    while idx1 < len(group1):
        list[idx] = group1[idx1]
        idx1 += 1
        idx += 1
    while idx2 < len(group2):
        list[idx] = group2[idx2]
        idx2 += 1
        idx += 1
    return list

from pprint import pprint
pprint(merge_sorted(log))
#[['대구', '09:00:13'],
#  ['대구', '09:01:10'],
#  ['대전', '09:00:03'],
#  ['대전', '09:14:25'],
#  ['대전', '09:37:44'],
#  ['부산', '09:10:11'],
#  ['부산', '09:10:25'],
#  ['부산', '09:22:43'],
#  ['부산', '09:22:54'],
#  ['부산', '09:36:14'],
#  ['서울', '09:00:00'],
#  ['서울', '09:00:59'],
#  ['서울', '09:03:13'],
#  ['서울', '09:19:32'],
#  ['서울', '09:19:46'],
#  ['서울', '09:21:05'],
#  ['서울', '09:25:52'],
#  ['서울', '09:35:21']]
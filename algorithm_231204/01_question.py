# 1. sys.stdin.realine() ... rstrip() 에서 strip이 언제 사용되는지?
# 만약 정확하게 판단이 안되는 경우에는 rstrip()을 사용하지 않다가,
# 에러가 나면 rstrip()을 추가하는 형태로 공부하는 것을 권장합니다.

# 2. == , is
# ==는 데이터에 대한 비교, is는 메모리에 대한 비교
arr1 = [1, 2, 3, 4]
arr2 = arr1[:]
print(f"arr1은 {arr1}")
print(f"arr2는 {arr2}")
print(f"같니? {arr1 == arr2}")

# 3. 깊은 복사와 얕은 복사
# 얕은 복사는 리스트를 복사하는 것은 맞으나, 리스트 내에서 참조되는 요소들도 복사가 되는 형태는 아니다.
# 따라서 리스트 내에 있는 리스트는 원본 변경의 영향을 받게 된다.
# 깊은 복사는 원본 변경에 전혀 영향을 받지 않는다.

import copy

x_max_person = ['캐빈', '머라이어캐리', '산타', '눈사람']
x_max_object = ['트리', '양말', '오너먼트']
x_mas = [x_max_person, x_max_object, '캐롤', '나홀로집에', '눈싸움']

deep_x_mas = copy.deepcopy(x_mas) # 깊은 복사
shallow_x_mas = x_mas[:] # 얕은 복사

print(x_mas)
print(shallow_x_mas)
print(deep_x_mas)

x_mas[0].append('루돌프')
print(x_mas)
print(shallow_x_mas)
print(deep_x_mas)
# # 최대값 : 9개의 입력을 받아, 최댓값을 찾고, 그 위치를 반환
# n_list = [int(input()) for _ in range(9)]
# n_max = max(n_list)
# print(n_max)
# print(n_list.index(n_max) + 1)

n_list = []
for _ in range(9):
    n_list.append(int(input()))
n_max = n_list[0]
max_index = 1
for i in range(len(n_list)):
    if n_max < n_list[i]:
        n_max = n_list[i]
        index = i + 1
print(n_max)
print(index)
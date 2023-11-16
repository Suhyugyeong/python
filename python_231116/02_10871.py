# X 보다 작은 수
N, X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

# A 안에서 X보다 작은 수를 결과물로 출력
result = [i for i in A if i < X]
# spread operator인 *을 사용하면,
# 리스트의 요소를 unpacking해서 출력할 수 있습니다.
print(*result)
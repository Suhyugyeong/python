X = int(input())
A = [int(i) for i in input().split()]

for i in range(len(A)) :
    if A[i] >= X :
        del A[i]

# 반복문이 동작하면서 배열의 크기가 변경되면 정상적인 반복이 불가능할 수 있다.
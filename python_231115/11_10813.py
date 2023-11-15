#공바꾸기


N, M = [int(i) for i in input().split()]

#N값 이용해서 바구니 만들기
balls = [i for i in range(1, N+1)]

# for i in range(1, N+1):
#     balls.append(i)

#M번 바꾸기
#"1 2"면 0번째와 1번째의 위치를 바꾼다..
for i in range(M):
    lt, rt = [int(i) - 1 for i in input().split()]
    balls[lt], balls[rt] = balls[rt], balls[lt]

print(*balls)

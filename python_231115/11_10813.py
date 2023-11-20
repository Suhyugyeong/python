#공바꾸기

# N, M = [int(i) for i in input().split()]
N, M = map(int, input().split())

#N값 이용해서 바구니 만들기
balls = [i for i in range(1, N+1)]

#balls= []
# for i in range(1, N+1):
#     balls.append(i)

#M번 바꾸기
#"1 2"면 0번째와 1번째의 위치를 바꾼다..
for i in range(M):
    #네번을 돌리겠다, 근데 어떻게 돌리겠다?
    left, right = [int(i) - 1 for i in input().split()]
    #인덱스에 접근해서 요소를 바꿔주겠다..
    #사용자로부터 입력받은 두 공의 위치는 1부터 N까지지만, 리스트의 인덱스는 0부터 시작하기 때문에 1을 빼서 인덱스로 변환해야..
    balls[left], balls[right] = balls[right], balls[left]
    #두 공의 위치를 변경하기 위해서는 동시 할당을 통해 간단히 해결!

print(*balls)

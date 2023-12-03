import sys
N = int(sys.stdin.readline())
meeting = []

# N번만큼 반복해서 시작시간(start), 끝나는 시간(end) 가져오기
# (start, end)를 meeting 배열에 추가
for i in range(N):
    # start, end = map(int, sys.stdin.readline().split())
    start, end = [int(i) for i in sys.stdin.readline().split()]
    meeting.append((start, end))

# 1) end_time이 짧은 회의 순으로 정렬 sort(key lambda)
meeting.sort(key=lambda x:(x[1], x[0]))

cnt = 0
finish_time = 0
# 2) 정렬된 meeting 반복 -> i:
for i in meeting:
#   3) i로부터 start_time, end_time을 가져온다.
    start_time, end_time = i
#   4) 만약 start_time이 전에 finish_time보다 크거나 같으면:
    if start_time >= finish_time:
#       5) cnt 1 증가
        cnt += 1
#       6) finish_time을 end_time으로 변경
        finish_time = end_time
        
# 7) cnt를 출력
print(cnt)
import sys
N = int(sys.stdin.readline())
meeting = [] #회의 시작 종료 시간을 튜플로 묶어 리스트에 저장

# N번만큼 반복해서 시작시간(start), 끝나는 시간(end) 가져오기
# (start, end)를 meeting 배열에 추가
for i in range(N):
    # start, end = map(int, sys.stdin.readline().split())
    start, end = [int(i) for i in sys.stdin.readline().split()]
    meeting.append((start, end))

# 1) end_time이 짧은 회의 순으로 정렬 sort(key lambda)
meeting.sort(key=lambda x:(x[1], x[0]))
#회의를 종료 시간을 기준으로 먼저 정렬
#종료 시간이 같으면 시작 시간을 기준으로 정렬
#이를 통해 종료 시간이 빠른 회의 순서로 정렬됩니다.

cnt = 0 #최대한 많은 회의를 진행할 때의 회의 수를 저장하는 변수
finish_time = 0
# 2) 정렬된 meeting 반복 -> i:
for i in meeting:
#   3) i로부터 start_time, end_time을 가져온다.
    start_time, end_time = i
#   4) 만약 start_time이 전에 finish_time보다 크거나 같으면:
    if start_time >= finish_time:
#만약 현재 회의의 시작 시간(start_time)이 이전까지의 회의 중에서 가장 마지막으로 끝나는 시간(finish_time)보다 크거나 같다면, 
#해당 회의를 진행할 수 있으므로 cnt를 1 증가시키고, 
#finish_time을 현재 회의의 종료 시간(end_time)으로 갱신
#       5) cnt 1 증가
        cnt += 1
#       6) finish_time을 end_time으로 변경
        finish_time = end_time
        
# 7) cnt를 출력
print(cnt)
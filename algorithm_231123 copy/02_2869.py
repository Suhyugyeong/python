import sys

def snail_slow():
    A, B, V = [int(i) for i in sys.stdin.readline().split()]
    now = 0
    day = 0
    while now < V:
        day += 1
        now += A # 낮이 되었습니다.
        if now >= V:
            break
        now -= B # 밤이 되었습니다.
    print(day)
    
def snail_fast():
    A, B, V = [int(i) for i in sys.stdin.readline().split()]
    every_day = A - B
    real_v = V - B
    day = real_v // every_day
    if real_v % every_day != 0:
        day += 1
    print(day)
snail_fast()
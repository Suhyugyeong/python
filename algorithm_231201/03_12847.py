import sys

N, M = [int(i) for i in sys.stdin.readline().split()] # 5 3
pay = [int(i) for i in sys.stdin.readline().split()] # 10 20 30 20 10

window = sum(pay[:M])
max_pay = window
for i in range(N - M):
    window += pay[i+M]-pay[i]
    max_pay = max(max_pay, window)

# window1 = sum(pay[0:3])
# window1 += pay[3] - pay[0] 
# window1 += pay[4] - pay[1]

print(max_pay)
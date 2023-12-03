import sys
N, m = [int(i) for i in sys.stdin.readline().split()]
pay = [int(i) for i in sys.stdin.readline().split()]

start = 0
sum = sum(pay[:m])
max_sum = sum

while m < N:
    sum += pay[m] - pay[start]
    max_sum = max(max_sum, sum)
    start += 1
    m += 1
print(max_sum)
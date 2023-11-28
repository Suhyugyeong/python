import sys
from collections import deque

N = int(sys.stdin.readline())
balloon = deque(enumerate([int(i) for i in sys.stdin.readline().split()]))
while balloon:
    move = balloon.popleft()
    if move[1] > 0:
        balloon.rotate(-(move[1] - 1))
    else:
        balloon.rotate(-move[1])
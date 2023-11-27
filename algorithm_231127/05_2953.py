import sys

def i_am_cook():
    sum_scores = []
    for _ in range(5):
        score = [int(i) for i in sys.stdin.readline().split()]
        sum_scores.append(sum(score))
    # sum_scores = [sum([int(i) for i in sys.stdin.readline().split()]) for _ in range(5)]
    print(sum_scores.index(max(sum_scores)) + 1, max(sum_scores))
    
i_am_cook()
# 별 찍기 _ while

star = int(input())

i = 1
while i < star + 1 : 
    print(" " *(star - i) + "*" * ((2 * i) - 1))
    i += 1

i -= 1

while i > 0 :
    print(" "*(star - i + 1) + "*" * (((i * 2) - 1) - 2))
    i -= 1
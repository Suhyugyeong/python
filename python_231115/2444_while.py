#while문
star = int(input())
i = 0

while i < star :
    print(" " * (star - i), "*" * (i * 2 + 1))
    i += 1
    
while i + 1 > star :
    print(" " * (i + 1), "*" * ((2 * star -1) - (2 * i)))
    i += 1

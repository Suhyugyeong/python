#while문
star = int(input())
i = 0

while i < star :
    print(" " * (star - i), "*" * (i * 2 + 1))
    i += 1
    
while i + 1 > star :
    print(" " * (i + 1), "*" * ((2 * star -1) - (2 * i)))
    i += 1

#

star = int(input())

i = 1
while i < star + 1 : 
    print(" " *(star - i) + "*" * ((2 * i) - 1))
    i += 1

i -= 1

while i > 0 :
    print(" "*(star - i + 1) + "*" * (((i * 2) - 1) - 2))
    i -= 1
    
    #

star = int(input())

i = 1
while i < star + 1:
    print(" " * (star -1) + "*" * (2 * i - 1))
    i += 1

i = 1
while i < star:
    print(" " * i + "*" + ((2 * star - 1) - (2 * i)))
    i += 1
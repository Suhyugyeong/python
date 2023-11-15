year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)

# 1900 -> 윤X (4의 배수 O, 400의 배수 X)
# 2000 -> 윤O (4의 배수 O, 400의 배수 O)
# 2012 -> 윤O (4의 배수 O, 100의 배수 X)
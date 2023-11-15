#n 입력

#구구단 출력
#for문

number = int(input())

for i in range(1, 10):
    result = number * i
    print(f"{number} * {i} = {result}")
    print(number, "*", i, "=", number * i)
    
    
#while문
number = int(input())
while i < 10 :
    print(f"{number} * {i} = {number*i}")
    i += 1
    
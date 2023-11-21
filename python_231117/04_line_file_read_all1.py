f = open("hello10.txt", "r", encoding="utf-8")
while True :
    line = f.readline() #readline에 더 이상 읽을 라인이 없는 경우, None 출력
    if not line:
        break
    print(line.rstrip())
f.close()

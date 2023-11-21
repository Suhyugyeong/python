#텍스트 인코딩(한글인 경우)
f = open("hello10.txt", "a", encoding = "utf-8")
for i in range(11, 20+1):
    data = f"안녕{i}~! \n"
    f.write(data)
f.close()
#실행해야지 hello10.txt 파일에 append 되는거임
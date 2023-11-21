f = open("hello10.txt", "r", encoding="utf-8")
#한국어 섞여있을 때, encoding=utf-8 해야지 에러가 안 뜸..
#'cp949' codec can't decode byte 0xec in position 77: illegal multibyte sequence
line = f.readline().rstrip()
#첫번째것만 나옴..
print(line)
f.close()

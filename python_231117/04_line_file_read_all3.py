
f = open("hello10.txt", "r")
data = f.read()
#read 함수 사용하면 파일 내용을 한번에 다 불러옴 
#만약에 파일의 크기가 트다면, 메모리의 사용이 커진다..
print(data)
f.close()

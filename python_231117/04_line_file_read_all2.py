f = open("hello10.txt", "r", encoding="utf-8")
#f라는 파일의 변수는 순회가 가능한 객체다.. iterable 숫자는 안되니까 range를 설정하는거고, 문자열 list 다 됐죠..
for i in f:
    print(i.rstrip())
f.close()

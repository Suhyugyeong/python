# with open() as f:
#앞으로는 이 방법으로 쓸 것이니, 이걸 기억해두기.. 앞으로 close() 안 써요..

with open("with.txt", "a", encoding="utf-8") as f:
    f.write("with블록을 벗어나는 순간, 파일 객체 f가 자동으로 close됩니다.")
#f.write 더 추가해도 가능한..

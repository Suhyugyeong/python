f = open("hello10.txt", "r")
line = (f.readline().rstrip())
#첫번째것만 나옴..
print(line)
f.close()
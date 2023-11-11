# msg = input()

# is_number =False
# if input("숫자를 입력했나요? 맞으면1, 아니면 2 \n") == "1":
#     msg = int(msg)
#     if msg:
#         print(msg)
#     else:
#         print("false인 경우에는 출력되지 않습니다.")
        
print(bool(1))
print(bool("안녕"))
print(bool("파이선"))
print(bool(-5))
print(bool(0.025))
print(bool(" "))
print(bool(""))#얘만 false임
print(bool("누가 쉽대?"))
print(bool(78))

age = int(input("나이를 입력하세요.\n"))
if age  >= 20:
    print("입장 가능한 연령입니다.")
elif age >= 15:
    print("제한된 입장이 가능합니다")
else : 
    print("입장이 불가합니다.")
    


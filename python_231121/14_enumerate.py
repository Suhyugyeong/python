rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

enum_rainbow = enumerate(rainbow)

print(enum_rainbow)
#<enumerate object at 0x000001D850F3E660>

for i in enum_rainbow:
    print(i)
#(0, '빨') 이런식으로 나옴 
#이 식은 꼭 외워두기!! 

print(list(enum_rainbow))
#[]
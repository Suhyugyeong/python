def hello_names(count = 1, *names):
    for name in names:
        print("Hello" * count, name)

# hello_names('손흥민', '이강인', '황희찬', 2)
hello_names(2, '손흥민', '이강인', '황희찬')
#가변매개변수/키워드인자 이 순서가 맞다..!
#작동은 하나, 권장하지 않는다...

#count
# hello_names(count = 2, '손흥민', '이강인', '황희찬')
# hello_names('손흥민', '이강인', '황희찬', count = 2)
# hello_names('손흥민', '이강인', '황희찬')

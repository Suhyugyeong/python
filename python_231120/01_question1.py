def hello_names(count = 1, *names):
    for name in names:
        print("Hello" * count, name)
        
hello_names('손흥민', '이강인', '황희찬')
hello_names(2, '손흥민', '이강인', '황희찬')
def hello_names(count = 1, *names):
    for name in names:
        print("hello" * count, name)
        
        hello_names('손흥민', '이강인', '황희찬', 2)
        #오작동 작동은 하지만
        hello_names(2, '손흥민', '이강인', '황희찬')
        #오작동 작동은 하지만
        # hello_names(count =2, '손흥민', '이강인', '황희찬')
        #에러
        hello_names('손흥민', '이강인', '황희찬', count =2)
        hello_names('손흥민', '이강인', '황희찬')
        
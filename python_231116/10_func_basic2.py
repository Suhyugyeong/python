def hello(name = '', count = 1):
    for _ in range(count):
        print("Hello", name)

hello()
hello('손흥민')
hello('이강인', 2)
hello(count=4) # hello('', 4)

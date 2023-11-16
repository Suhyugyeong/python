def hello1():
    print("Hello")
    
def hello2(name):
    print(f"Hello~ {name}")

def hello3(name, count):
    for _ in range(count):
        print(f"Hello! {name}")

hello1()
hello2("Kim")
hello3("Lee", 3)
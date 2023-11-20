def get_hierarchy(exception_class, indent = 0):
    # 들여쓰기를 기준으로 예외 클래스 이름을 출력시키기!
    print(indent * " ", exception_class.__name__)
    subclasses = exception_class.__subclasses__()
    for subclass in subclasses:
        get_hierarchy(subclass, indent + 2)
        
get_hierarchy(BaseException)
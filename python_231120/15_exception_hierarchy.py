#특정 예외 클래스를 기준으로 해당 예외 클래스의 하위 클래스들의 계층 구조를 출력
#재귀적으로 각 예외 클래스와 그에 속한 하위 클래스를 출력

def get_hierarchy(exception_class, indent = 0):
    # indent는 들여쓰기 수준을 나타내며, 기본값은 0
    print(indent * " ", exception_class.__name__)
    subclasses = exception_class.__subclasses__()
    for subclass in subclasses:
        get_hierarchy(subclass, indent + 2)
        
get_hierarchy(BaseException)
#파이썬에서 모든 내장 예외 클래스의 최상위 부모 클래스
#모든 내장 예외 클래스는 BaseException 클래스에서 상속받아 만들어지고, 이를 통해 예외 클래스 간 공통된 특성을 공유할 수 있음.
#예외 처리 시 모든 예외 클래스의 최상위 클래스로 활용되며, 개발자가 새로운 예외를 정의할 때 이를 상속받는 것이 일반적


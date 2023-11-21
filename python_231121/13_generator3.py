a = [n for n in range(100)]
b = range(100)

print(len(a))
print(len(b))
print(a)
print(b)

import sys
print(sys.getsizeof(a)) #920
print(sys.getsizeof(b)) #48 (10, 100 , 10000 무슨 숫자든 간에 무조건 48)
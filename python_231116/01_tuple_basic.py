my_tuple = ()
print(my_tuple)
print(type(my_tuple))

my_int = (1)
my_tuple = (1,)
print(my_tuple)
print(type(my_tuple))

my_tuple1 = (1, 2, 3)
my_tuple2 = 1, 2, 3

print(my_tuple1)
print(my_tuple2)
print(my_tuple1 == my_tuple2)

my_tuple3 = ('a', 'b', ('c', 'd'))
print(my_tuple3[1])
# my_tuple3[1] = 'B' -> 에러!! 수정 불가능!
# del my_tuple3[0] -> 에러!! 삭제 불가능!

my_tuple4 = (1, 2, 4, 8)
odd, *even = my_tuple4
print(odd, even)
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

my_int = (1)
print(type(my_int))
#<class 'int'>
my_tuple1 = (1,)
print(type(my_tuple1))

my_tuple2 = 1,2,3
#<class "tuple">
my_tuple3 = (1,2,3)
print(type(my_tuple2))
print(type(my_tuple3))
print(my_tuple2 == my_tuple3)

tuple_list = ("a", "b", ("c", "d", "e"))
print(tuple_list[0])
#tuple_list[0] = "가" => 에러!! 수정 불가능!!
# del tuple_list[0] => 에러!! 삭제 불가능!!

my_tuple4 = (1,2,4,8)
odd, *even = my_tuple4
print(odd, even)
#[2,4,8] list로 나옴
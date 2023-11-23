str = 'apple'
print(id('apple'), id('banana'), id(str))

str = 'banana'
print(id('apple'), id('banana'), id(str))

# str[0]= 'b' 불변!!!!!
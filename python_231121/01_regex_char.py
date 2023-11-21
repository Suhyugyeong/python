from regex_check import match_check

match_check("[abc]", "alphabet")
match_check("[abc]", "computer")
match_check("[abc]", "smart")

match_check("[0-9]", '123')
match_check("[^0-9]", '123') #false

match_check("[a-z]", "Alphabet")
match_check("[^a-zA-Z]", "Alphabet") #false

match_check("[a-zA-Z0-9]","Gildong123")
match_check("[^a-zA-Z0-9]","Gildong123") #false
match_check("[\s]", "Hello World")

match_check("[가-힣]", "홍길동")
#모든 한글은 가-힣 범위
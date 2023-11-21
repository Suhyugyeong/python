from regex_check import match_check

match_check("go*d", "gd")
match_check("go*d","god")
match_check("go*d", "goooooooood")

match_check("go+d", "gd") #f
match_check("go+d", "god")
match_check("go+d", "gooooood")

match_check("g[A-Z]+d", "goooooooooooood") #f
match_check("g[A-Z]+d", "gOOOOOOOOOOOOd")

match_check('g[A-Z]+d', 'gABCd') # T
match_check('g[A-Z]+d', 'gAaBbCd') # F
match_check('g[A-Z]+d', 'gAaBBbCd') # F
from regex_check import match_check


match_check("a.b","a0b")
match_check("a.b","a.b")
match_check("a.b","aaab") #true임 
match_check("a.b","a\nb") #f
match_check("a.b","a\tb") 
match_check("a.b","a   b") #f
match_check("a.b","a b")
match_check("a.b","acb") 
match_check("a.b","a\n\tb") #f

match_check("a[.]b","a.b") 
match_check("a[.]b","a0b") #f
match_check("a[.]b","a\nb") #f











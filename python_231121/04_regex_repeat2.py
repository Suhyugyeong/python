from regex_check import match_check

match_check("hel{2}o", "hello") #true

match_check("hel{1,3}","heo") #f
match_check("hel{1,3}","helo")
match_check("hel{1,3}","hello")
match_check("hel{1,3}","helllo")
match_check("hel{1,3}","hellllo") #f

match_check("hell?o","helo")
match_check("hell?o","hello")
match_check("hell?o","helllo") #f

match_check("hel{,3}o", "heo") #true 3이하니까 0도 가능한가보다..
match_check("hel{,3}o", "helo")
match_check("hel{,3}o", "hello")
match_check("hel{,3}o", "helllo")
match_check("hel{,3}o", "hellllo") #f

match_check("hel{3,}o", "hello") #f
match_check("hel{3,}o", "helllo")
match_check("hel{3,}o", "hellllo")

match_check("go{0,}d", "gd")
match_check("go{1,}d", "gd") #f
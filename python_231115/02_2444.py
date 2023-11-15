
#별찍기 for문

star = int(input())
# star = 5

for i in range(1, star+1):
    print(" "*(star - i), "*" * (i * 2 - 1))
    

#range를 통해 증가되고,,감소되는 걸 만듦

#등차수열

for i in range(1, star):
     print(" "* i , "*" * ((2 * star - 1) - (2 * i)))
     
     # -2 * n + 9 (an -b)
     


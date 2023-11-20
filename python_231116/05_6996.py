# 애너그램 체크 (feat. 딕셔너리)
# CASE_NUM = int(input())

# for _ in range(CASE_NUM):
#     word1, word2 = input().split()
#     d_word1 = {}
#     for i in word1:
#         if i in d_word1: d_word1[i] += 1
#         else : d_word1[i] = 1
            
#     d_word2 = {}
#     for i in word2:
#         if i in d_word2: d_word2[i] += 1
#         else : d_word2[i] = 1
    
#     if d_word1 == d_word2:
#         print(f"{word1} & {word2} are anagrams.")
#     else:
#         print(f"{word1} & {word2} are NOT anagrams.")
        

#sorted 함수 사용

CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split()

    # sorted_word1 = sorted(list(word1))
    # sorted_word2 = sorted(list(word2))
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    #둘 차이 없음.. 간단하게 하려면 list 생략하면 됨. 어차피 input().split()한 시점에서 list임..


    if sorted_word1 == sorted_word2:
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")
        

#제일 심플하게...내가 했다!!
CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split()
    if sorted(word1) == sorted(word2):
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")

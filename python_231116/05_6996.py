# 애너그램 체크 (feat. 딕셔너리)
CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split()
    d_word1 = {}
    for i in word1:
        if i in d_word1: d_word1[i] += 1
        else : d_word1[i] = 1
            
    d_word2 = {}
    for i in word2:
        if i in d_word2: d_word2[i] += 1
        else : d_word2[i] = 1
    
    if d_word1 == d_word2:
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")
# 애너그램 체크
CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split()
    if sorted(word1) == sorted(word2):
        print("{} & {} are anagrams.".format(word1, word2))
    else:
        print("{} & {} are NOT anagrams.".format(word1, word2))

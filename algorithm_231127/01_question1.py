# 애너그램 체크
CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split() # 구조분해할당
    word = word1, word2 # 리스트로 재병합 ([]를 생략하면 튜플로 병합된다)
    if sorted(word1) == sorted(word2):
        print("{} & {} are anagrams.".format(word1, word2))
    else:
        print("{} & {} are NOT anagrams.".format(word1, word2))
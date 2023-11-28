# 애너그램 체크
CASE_NUM = int(input())

for _ in range(CASE_NUM):
    word1, word2 = input().split() # 구조분해할당
    #파이썬에서 구조분해할당은 여러 값을 한 번에 변수에 할당하는 기능
    #튜플이나 리스트 같은 이터러블한 객체 다룰 때 유용하게 사용
    
    word = word1, word2 # 리스트로 재병합 ([]를 생략하면 튜플로 병합된다)
    if sorted(word1) == sorted(word2):
        print("{} & {} are anagrams.".format(word1, word2))
    else:
        print("{} & {} are NOT anagrams.".format(word1, word2))

# str1 = input()
# str2 = input()
# if sorted(str1) == sorted(str2):
#     print(str1, "&", str2, "are anagrams.")
# else:
#     print(str1, "&", str2, "are NOT anagrams.")

#애너그램 체크
CASE_NUM = int(input())


words1, words2 = input().split()
words1 = sorted(words1)
words2 = sorted(words2)
if words1 == words2:
    print("{} & {} are anagrams.".format(words1[0], words2[1]))
else : 
    print("{} & {} are NOT anagrams.".format(words1[0], words2[1]))
print(words1)
print(words2)


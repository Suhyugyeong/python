alpabet = ["a", "b", "c", "d", "e"]

# vow = [alpabet[0], alpabet[2]]
# vow = alpabet[:] #리스트복제 
# vow = alpabet[0:5:4] #시작, 끝, 스텝
vow = [alpabet[0], alpabet[4]]
consonant = alpabet[1:4]
#consonant = [alpabet[1], alpabet[2], alpabet[3]]

#인덱싱은 요소를 반환, 슬라이싱은 리스트를 반환

new_alpabet = [vow, consonant]
print(new_alpabet)

print(new_alpabet[0][1])
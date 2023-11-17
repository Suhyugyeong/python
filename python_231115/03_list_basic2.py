alpabet = ["a", "b", "c", "d", "e"]

vow = [alpabet[0], alpabet[2]]
vow = alpabet[:] #리스트복제 
vow = alpabet[0:5:4] #시작, 끝, 스텝 / 마지막수는 항상 -1해서 뽑는다!!
vow = [alpabet[0], alpabet[4]]

consonant = alpabet[1:4]
#['b', 'c', 'd']

#인덱싱은 요소를 반환, 슬라이싱은 리스트를 반환
#인덱싱은 주로 하나를 뽑을 때, 슬라이싱은 범위를 뽑을 때..

new_alpabet = [vow, consonant]
#여러개인 vow 중 맨마지막을 가져옴..
print(new_alpabet)
#[['a', 'e'], ['b', 'c', 'd']]
print(new_alpabet[0][1]) #e
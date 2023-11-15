num_list = [1,2,3,4]
#방법1. 기존의 리스트를 이용해 새로운 리스트를 생성 
even_list = []
for i in num_list:
    #for는 그냥 반복하기 위해 계속 쓴다.
    even_list.append(2*i)
#[2,4,6,8]

#혁명적 방법2. 기존의 리스트를 이용해 새로운 리스트를 생성
#빈 배열을 만들어 줄 필요도, append 함수를 호출할 필요가 없다..
even_list = [2*i for i in num_list]
print(even_list)
#[2,4,6,8]

#even_list = [2*i for i in num_list]
#expression: 각 요소에 대한 변환식 또는 동일하게 반환할 표현식입니다.
#item: iterable에서 가져온 요소를 나타내는 변수입니다.
#iterable: 반복 가능한 객체(리스트, 튜플 등)입니다.
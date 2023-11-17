practice_list = [1, 2 , 3, "파이", "apple", ["가", "나", "다", "라"]]

#리스트의 "파이"를 숫자 3.14로 바꾸어요
# practice_list[3] = 3.14
# print(practice_list)

#리스트의 3을 4, 8로 수정
# practice_list[2] = 4, 8
# print(practice_list)
#(4,8)로 들어가고..
#괄호를 생략하면 튜플로 인식한다..

# practice_list[2] = [4, 8]
# print(practice_list)
#[4,8]로 들어감.. 

practice_list[2:3] = 4, 8
print(practice_list)
practice_list[2:3] = [4, 8]
print(practice_list)

# practice_list[2:3] = [4,8]
# print(practice_list)
#왜 후자의 방법을 썼을 때 4, 8이 들어가는 방식이 똑같을까? 
#예를 들어 전자는 숫자일 때 (4,8) / 리스트일 때 [4,8] 이런식으로 들어갔음.

#슬라이싱과 인덱싱을 구분해요~!!
# [1, 2, 4, 8, '파이', 'apple', ['가', '나', '다', '라']]
#"apple" 삭제하기
# practice_list[5] = []
# print(practice_list)
#위에거는 삭제가 아니라, 수정임

practice_list[5:6] = []
print(practice_list)
#이렇게 하면 삭제 됨

#[1, 2, 4, 8, '파이', ['가', '나', '다']]
#"라"를 삭제!
# practice_list[-1][-1:4] = []
#잘못된 코드 [-1:4]작아지는 순으로 슬라이싱 안 됨.. 결과는 나옴..
#[1, 2, 4, 8, '파이', ['가']]

# practice_list[-1][-1] = []
#맨마지막 리스트에 맨마지막 순서에 빈 리스트를 넣는다..

#이거는 안 되기 때문에 del을 쓴다
del practice_list[-1][-1]
print(practice_list)

#[1, 2, 4, 8, '파이', ['가', '나', '다']]
#"나", "다" 삭제!
del practice_list[-1][1:]
print(practice_list)

#[1, 2, 4, 8, '파이', ['가']]
#"가" 삭제!
# del practice_list[-1][:]
#[1, 2, 4, 8, '파이', []]
#[:]리스트 전체를 나타내는 슬라이싱
#리스트 안의 리스트를 비운다. 요소는 지워지나 리스트는 남아있음..

del practice_list[-1]
#이렇게 해야 요소와 함께 리스트가 삭제가 됨..
print(practice_list)
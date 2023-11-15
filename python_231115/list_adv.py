practice_list = [1, 2 , 3, "파이", "apple", ["가", "나", "다", "라"]]

#리스트의 "파이"를 숫자 3.14로 바꾸어요
# practice_list[3] = 3.14
# print(practice_list)

#리스트의 3을 4, 8로 수정
# practice_list[2] = 4, 8
# print(practice_list)
#(4,8)로 들어가고..
# practice_list[2] = [4, 8]
# print(practice_list)
#[4,8]로 들어감.. 
practice_list[2:3] = 4, 8
print(practice_list)
# practice_list[2:3] = [4,8]
# print(practice_list)

#슬라이싱과 인덱싱을 구분해요~!!

#"apple" 삭제하기
practice_list[5] = []
#위에거는 삭제가 아니라, 수정임
practice_list[5:6] = []
#이렇게 하면 삭제 됨


#"라"를 삭제!
# practice_list[-1][-1:4] = []
# practice_list[-1][-1] = []
#이거는 안 되기 때문에 del을 쓴다
del practice_list[-1][-1]
print(practice_list)

#"나", "다" 삭제!
del practice_list[-1][1:]
print(practice_list)

#"가" 삭제!
# del practice_list[-1][:]
# 이렇게 하면 또 배열 자체는 공란으로 남아버림..
del practice_list[-1]
print(practice_list)
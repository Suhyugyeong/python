num_list = [1,2,3,4]
#방법1. 기존의 리스트를 이용해 새로운 리스트를 생성 
# even_list = []
# for i in num_list:
#     even_list.append(2*i)

#혁명적 방법2. 기존의 리스트를 이용해 새로운 리스트를 생성
even_list = [2*i for i in num_list]
print(even_list)
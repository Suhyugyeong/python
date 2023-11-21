#순차탐색을 통한 모든 위치 반환

# num_list = [int(i) for i in input().split()]
# value = int(input())

# def find_my_num(list, value):#매개변수
#     result_list = []
#     for i in list:
#         if value == i:
#             result_list.append(i)
#     return  result_list

# result = find_my_num(num_list, value)#인자: 넘리스트에서 value값을 찾을거다..! 
# 인자에 값을 안 넣으면 missing 2 required positional arguments: 'num_list' and 'value'
    
# print(f"{result}")

num_list = [int(i) for i in input().split()]
value = int(input())

def find_my_num(num_list, value):#매개변수
    result_list = []
    for i in num_list:
        if value == i:
            result_list.append(i)
    return  result_list

result = find_my_num(num_list, value)#인자: 넘리스트에서 value값을 찾을거다..! 인자 값을 똑같이 넣어줘도 됨..
    
print(f"{result}")

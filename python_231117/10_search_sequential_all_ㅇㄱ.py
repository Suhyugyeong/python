#순차탐색을 통한 모든 위치 반환


num_list = [int(i) for i in input("여러개의 값 입력하세요.").split()]
value = int(input("찾을 값 입력하세요."))

def find_my_num(list, value):
    result_list = []
    for i in list:
        if value == i:
            result_list.append(i)
        return  result_list

result = find_my_num(list, value)
    
print(f"{result}")

#GPT가 풀어줌..

# user_input = input("리스트의 값을 입력하세요 (공백으로 구분): ")
# my_list = [int(x) for x in user_input.split()]

my_list = [int(x) for x in input("리스트의 값을 입력하세요 (공백으로 구분):").split()]

# 타겟 값 입력받기
target_value = int(input("찾고자 하는 값을 입력하세요: "))

def sequential_search(input_list, target):
    indices = []
    for i, value in enumerate(input_list):
        if value == target:
            indices.append(i)
    return indices


# 순차 탐색 실행
result = sequential_search(my_list, target_value)

print(f"{result}")

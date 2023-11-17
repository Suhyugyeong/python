#첫째줄 자연수 하나
#두번째줄 n개 정수 (5 => 1~5) => 하나의 수를 받아서 for문 씀?
#세번째줄 자연수 하나
#네번째줄 m개의 수 (5 => 5개의 랜덤 수?)
num1 = int(input())
num1_list = [int(i) for i in input("여러의 값을 입력하세요.").split()]

num2 = int(input())
num2_list = [int(j) for j in input("여러의 값을 입력하세요.").split()]

#m개의 줄에 답을 출력한다? m번 돌린다? 
def search(num1_list, num2_list):
    for value in num2_list:
        if value in num1_list:
            print(1)
        else:
            print(0)

#결과 출력

#gpt가..
num1 = int(input())
num1_list = [int(i) for i in input().split()]

num2 = int(input())
num2_list = [int(j) for j in input().split()]

def search(list1, list2):
    for value in list2:
        if value in list1:
            print(1)
        else:
            print(0)

search(num1_list, num2_list)


#gpt(2)
num1 = int(input())
num1_list = [int(i) for i in input().split()]

num2 = int(input())
num2_list = [int(j) for j in input().split()]

def search(list1, list2):
    result = []  
    for value in list2:
        if value in list1:
            result.append(1)
        else:
            result.append(0)
    print(result)

search(num1_list, num2_list)


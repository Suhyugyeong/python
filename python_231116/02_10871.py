#입력된 리스트 A에서 X보다 작은 값들만을 가지고 새로운 리스트 result를 만들어 출력

N, X =[int(i) for i in input().split()]
#N과 X에 순서대로 할당
A = [int(i) for i in input().split()]


#A 안에서 X보다 작은 수를 결과물로 출력

result = [i for i in A if i < X]
print(*result)
#spread operator인 *을 사용하면, 리스트의 요소를 언패킹해서 출력할 수 있다..
#예를 들어, print(result) = [1,3,5]로 출력된다면, print(*result) = 1 3 5 이렇게 출력

# result = [j for j in range(A) if j<X]
#range(숫자)가 들어가야 되기 때문에 그냥 리스트 바로 뽑을거면 A 넣으면 됨

#전화번호 패드 숫자를 이용해 만들 수 잇는 모든 가능한 문자열 조합을 찾기 위해 DFS 사용해 백트래킹 기법..
#백트래킹은 문제의 해결을 위해 후보를 탐색하다 조건을 만족할 것 같지 않으면 다시 이전 단꼐로 돌아가 다시 후보를 탐색
#주로 깊이 우선 탐색(DFS)과 함께 사용하머, 결정 문제나 조합 최적화 문제 등에 유용
class Solution:
    def letter_combinations(self, digits: str) -> list[str]: #digits을 문자로 받겠다
        letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = [] #가능한 문자열 조합을 저장할 빈 리스트
        word = "" #현재까지 탐색된 문자열을 저장할 변수를 초기화
        if digits == "":
            return result
        #숫자 문자열이 비어있으면 빈 리스트 반환 후 종료
        
        def dfs(word): #깊이 우선 탐색을 수행하는 내부함수 dfs/ 현재까지 탐색된 문자열을 받아 가능한 모든 조합 찾기
            # 입력값(digits)의 길이와 word의 길이를 비교해서 같으면 백트래킹
            if len(word) == len(digits):
                result.append(word)
                return
            # 입력값(digits)에 대한 딕셔너리 내 리스트를 확인
            # 1인 경우에는 [2, 3, 4]
            for i in letter_dict[digits[len(word)]]:
                dfs(word + i) # word에 문자가 하나씩 추가되고, 재귀 호출
        dfs(word)
        return result

sol = Solution()
digits = "23"
result = sol.letter_combinations(digits)
print(result)
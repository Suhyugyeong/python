#전화번호 패드의 숫자를 이용해 만들 수 있는 모든 가능한 문자열 조합을 찾기
class Solution:
    def letter_combinations(self, digits: str) -> list[str]: 
        #이 메서드는 전화번호 문자열을 입력 받아 가능한 모든 문자열 조합을 담은 리스트를 반환
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
        result = []
        
        if digits == "":
            return result
        # 스택을 생성
        stack = [""]
        
        while stack: #stack이 비어있지 않는 동안 반복
            word = stack.pop()
            if len(word) == len(digits):
                #만약 현재 꺼낸 문자열의 길이가 입력 숫자 문자열의 길이와 같다면, 
                #이는 하나의 가능한 조합이므로 결과 리스트에 추가
                result.append(word)
            if len(word) < len(digits):
                #현재 문자열의 길이가 입력 숫자 문자열의 길이보다 작다면, 
                #새로운 문자를 추가하여 가능한 조합을 생성
                for i in letter_dict[digits[len(word)]]:
                    #현재 문자열의 길이에 해당하는 숫자에 대응하는 문자들을 순회하면서, 
                    #각 문자를 현재 문자열에 덧붙인 새로운 문자열을 스택에 추가
                    stack.append(word + i)        
        return result

sol = Solution()
digits = "23"
result = sol.letter_combinations(digits)
print(result)
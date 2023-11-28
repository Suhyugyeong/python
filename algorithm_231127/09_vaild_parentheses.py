class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        # 딕셔너리 형태, 키와 값 쌍으로.. ) 에 ( 매핑..
        # 이 정보를 활용해 괄호의 짝이 맞는지 확인
        
        for i in s:
            if i not in mapping: # 여는 괄호가 들어왔을 때
                stack.append(i) # 스택에는 여는 괄호만이 들어간다!!!            
            elif not stack or mapping[i] != stack.pop(): # 닫는 괄호가 들어왔는데,
                return False #스택이 비어있거나, 매핑이 안 맞는 경우 False반환
        return bool(not stack) #마지막에 스택이 비어있음 True, 비어있지 않음 False 반환
    
sol = Solution()
result = sol.is_valid("(){}[]")
print(result)
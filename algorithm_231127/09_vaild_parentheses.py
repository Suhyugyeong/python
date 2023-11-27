class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        for i in s:
            if i not in mapping: # 여는 괄호가 들어왔을 때
                stack.append(i) # 스택에는 여는 괄호만이 들어간다!!!            
            elif not stack or mapping[i] != stack.pop(): # 닫는 괄호가 들어왔는데,
                return False
        return bool(not stack)
    
sol = Solution()
result = sol.is_valid("(){}[]")
print(result)
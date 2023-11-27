class Solution:
    def reorder_log_files(self, logs: list[str]) -> list[str]:
        # function 함수명(매개변수) {
        #   return 반환값
        #}
        
        # 함수명 = 매개변수 => 반환값
        # def temp(log):
        #     return log.split()[1:], log.split()[0]
        # temp = lambda x : (x.split()[1:], x.split()[0])
        
        letter_logs = [] # ["let1 art can", "let2 own kit dig","let3 art zero"]
        digit_logs = []
        for i in logs:
            if i.split()[1].isalpha():
                letter_logs.append(i)
            else:
                digit_logs.append(i)
        letter_logs.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs

logs = ["dig1 8 1 5 1","let1 천다영","dig2 3 6","let2 신혜인","let3 정준혁"]
sol = Solution()
print(sol.reorder_log_files(logs))
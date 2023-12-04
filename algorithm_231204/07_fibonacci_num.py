class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        if n in [0, 1]:
            return n
        self.fib(n - 1) + self.fib(n - 2)
    
sol = Solution()
result = sol.fib(1)
print(result)
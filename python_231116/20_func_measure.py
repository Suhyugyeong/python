import time

start = time.time()

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# fib(30)

end = time.time()
print("{0:0.20} sec.".format(end -start))
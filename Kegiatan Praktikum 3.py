# def fibo(n):
#     f1, f2 = 1, 1
#     print(f1, ", ", f2, ", ", end='')
#     for i in range(2, n):
#         fib = f1 + f2
#         f1 = f2
#         f2 = fib
#         print(fib, ", ",end='')
# fibo(7)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(7))


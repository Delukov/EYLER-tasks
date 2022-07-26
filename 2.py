def fib(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
i = 0
s = 0
while fib(i) < 4000000:
    if (fib(i) % 2) == 0:
        s += fib(i)
    i += 1
print(s)

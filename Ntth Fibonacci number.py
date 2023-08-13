def fibonacci(n):
    a = 1
    b = 1
    num = 0
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2,n):
            num = a + b
            a = b
            b = num
        return num%1000000007

print(fibonacci(14521))
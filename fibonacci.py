def fibo(n):
    a=0
    b=1
    n=n-2
    while n:
        c=a+b
        a,b=b,c
        n=n-1
    if n == a or b:
        print('it is a fibonacci')
    else:
        print('it is not a fibonacci')
fibo(10)

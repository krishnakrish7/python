##python program to find wether the given number is fibonacci or not
a=0
b=1
c=0
i=0
while True:
    c=a+b
    a,b=b,c
    i+=1
    if c==n:
        print("fibonacci")
        break
    else:
        if c>n:
            print("not fibonacci")
            break

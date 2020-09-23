##write a logic to check wether given number is happy number or not
##a number is said to be happy if it yields 1 or 7 when replaced by the sum of squares of itd digit repeatedly.if this process
##results in an endless cycle of number containing any single digit other than 1 or 7
##then the number will b an unhappy number.
#python code
n= int(input("enter a number"))
res=0
while True:
    d=n%10
    res=res+d*d
    n=n//10
    if res<9 and n==0:
        break
    if n==0:
            n=res
            res=0
if res==1 or res==7:
    print("happy")
else:
    print("unhappy")

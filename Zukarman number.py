##Zukarman
##Zuckerman number is a number which is divisible by the productof the digits
##n = 28 then 2*8=16 and 28%16=0
def is_Zukarman(n):
    product = 1
    tem = n
    while n:
        r = n%10
        n = n//10
        product=product*r
    if tem%product==0:
        return True
    return False
print(is_Zukarman(28))

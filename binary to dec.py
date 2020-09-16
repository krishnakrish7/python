n = 101
base = 1
dec = 0
while n:
    r=n%10
    n=n//10
    dec+=r*base
    base=base*2
print(dec)

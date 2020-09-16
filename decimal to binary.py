n = 15
z = []
while n:
    z.append(n%2)
    n = n // 2
z = z[::-1]
print(*z)

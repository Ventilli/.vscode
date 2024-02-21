n = int(input())

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n*3 + 1
    print(n)
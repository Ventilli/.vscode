n, m = int(input()), int(input())
nw, mw = input().split(), input().split()
nm = []
i1 = 0
i2 = 0

while i1 < n or i2 < m:
    if n - i1 != 0:
        nm.append(n[i1])
    elif m - i2 != 0:
        nm.append(m[i2])
    else:
        break
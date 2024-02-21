def fed(n: str):
    if n.isdigit():
        return False
    else:
        return True


print(*filter(fed, 'ahdsh1938e8dgs8'))

print(*map(lambda x: x * 1.61, [1, 2.3, 1.6]))

def NOD(a, b, mid = 0):
    if a != b:
        if a > b:
            mid = a - b
            if mid > b:
                return NOD(mid, b)
            else:
                return mid
        else:
            mid = b - a
            if mid > a:
                return NOD(a, mid)
            else:
                return mid
    else:
        return a

print(*map(lambda x, n: x * n // NOD(x, n), [4,24], [24,4]))




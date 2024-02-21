def nums_of_fibanachy(n, i = 0, medium = 1, end = 1):
    if i + 1 == n:
        return end
    else:
        return nums_of_fibanachy(n, i + 1, end, medium + end)


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
    
def NOK(a, b, nod):
    return a * b // nod

a = 12
b = 8
print(NOD(a, b))
print(NOK(a, b, NOD(a, b)))    
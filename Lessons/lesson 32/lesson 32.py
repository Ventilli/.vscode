def summ(n, a):
    if a == 0:
        return 0
    if a > 0 and n[a - 1] % 2 != 0:
        return 0 + summ(n, a - 1)
    if a > 0 and n[a - 1] % 2 == 0:
        return n[a - 1] + summ(n, a - 1)
lst = [1,2,3,4,5,6,7]
lenght = 7



def minimum(lst, lenght = len(lst)):
    smallest = lst[0]
    if lst[lenght] < smallest:
        smallest = lst[lenght]
    else:
        return minimum(lst, lenght - 1)
        
print(summ(lst, lenght))
print(minimum([4, 5, 9, 1], 3))
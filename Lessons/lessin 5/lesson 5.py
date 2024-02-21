# print('чет') if int(input()) % 2 == 0 else print('неч')



subject = 'математика'
subject_iter = iter(subject)
i = 0
while i < len(subject):
    print(next(subject_iter))
    i += 1
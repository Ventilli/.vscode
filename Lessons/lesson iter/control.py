vegetables = ["грязное яблоко", "грязная груша", "грязный банан"]
def wash(v):
    clean_vegs = []
    for x in v:
        clean_veg = x[8:]
        clean_vegs.append(clean_veg)
    return clean_vegs

def cutting(v):
    cut_vegs = []
    for i in v:
        sliced_veg = 'нарезанный ' + i
        cut_vegs.append(sliced_veg)
    return cut_vegs

def zapravka(v):
    v.append(input('Заправки: ').split())
    return v

tarelka = zapravka(cutting(wash(vegetables)))
print(f'Салат из {tarelka} уже на тарелке!')
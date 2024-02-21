from random import choice

digits = "1234567890"
symbols = '~`!@#$%^&*()_+-={}|[]\;:"<>?,./'
symbols_lower = 'qwertyuiopasdfghjklzxcvbnm'
symbols_upper = symbols_lower.upper()

print(choice(symbols))

lenght = 3

def paroll_generation(kolvo = int(input()), alphabet = input()):
    i = kolvo
    symbs = ''

    if alphabet == 'digits':
        symbs = digits
    elif alphabet == 'symbols':
        symbs = symbols
    elif alphabet == 'small letters':
        symbs = symbols_lower
    elif alphabet == 'big letters':
        symbs = symbols_upper
    else:
        return 1
    
    paroll = ''
    
    while i != 0:
        paroll += choice(symbs)
        i -= 1
    return paroll

while lenght != 0:
    print(paroll_generation())
    lenght -= 1
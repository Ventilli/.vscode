from random import randint

def s():
    try:
        with open(file = 'Lessons/files/poem.txt', mode = 'r', encoding = 'utf-8') as file:
            for line in file:
                        print(line)
    except:        
        print('ERROR (something is wrong, try again)')

def print_n_lines():
    try:
        with open(file = 'Lessons/files/poem.txt', mode = 'r', encoding = 'utf-8') as file:
            inputt = int(input())
            n = 0
            for line in file:
                if n < inputt:
                        print(line)
                else:
                    break
                n += 1
    except:        
        print('ERROR (something is wrong, try again)')

def randline():
    try:
        with open(file = 'Lessons/files/poem.txt', mode = 'r', encoding = 'utf-8') as file:
            l = 0
            n = 0
            for a in file:
                 n += 1
            print(n)
            n = randint(1, n)
            print(n)
            for line in file:
                l += 1
                if n == l:
                    print(line)           
    except:        
        print('ERROR (something is wrong, try again)')

# with open(file = 'Lessons/files/poem.txt', mode = 'r', encoding = 'utf-8') as read_file:
#     word = ''
#     words = []
#     for line in read_file:
#         for lettre in line:
#             if lettre != ' ' or lettre != '/n':
#                 word += lettre
#                 print(word)
#             if lettre == ' ' or lettre == '/n':
#                 words += word
#                 word = ''




randline()
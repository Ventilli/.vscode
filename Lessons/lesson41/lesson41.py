dell = input()

def Divison():
    try:
        1212312 / dell
    except:
        print('Something is wrong')
    else: 
        print('Answer: ', 123456 / dell)

def calculate(num1 = input(), num2 = input(), sign = input()):
    try:
        if sign == "+":
            return num1 + num2
        elif sign == "-":
            return num1 - num2
        elif sign == "*":
            return num1 * num2
        elif sign == "/":
            return num1 / num2
        elif sign == "//":
            return num1 // num2
        elif sign == "**":
            return num1 ** num2
        elif sign == "%":
            return num1 % num2
    except:
        return 'Something is wrong'
    
print(calculate())
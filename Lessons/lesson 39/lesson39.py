def memory1(func):
    print('Не забудь поесть')
    func()
def memory2():
    print("Но я уже опаздываю!")

memory1(memory2)

def decorator2(symbol):
    print(symbol * 30)
    def decorator1(func):
            
        def wrap():
            print('*' * 30)
            func()
            print('*' * 30)
            print(symbol * 30)
        return wrap
    return decorator1 


row = input()
symbol = input()


@decorator2(symbol)
def function():
    print(row)

function()
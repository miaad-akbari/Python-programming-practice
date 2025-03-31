# create functions for + - * / 

# condition for run + - * /

# get clients numbers

def sum(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def multiplication(number1 , number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

number1 = int(input('Please Enter your first number: '))

number2 = int(input('Please Enter your second number: '))

sel = input('Please select choice +\n  -\n *\n /\n  \n: ')

if sel == '+':
    print(number1, '+', number2, '=', sum(number1, number2))

if sel == '-':
    print(number1, '-', number2, '=', minus(number1, number2))

if sel == '*':
    print(number1, '*', number2, '=', multiplication(number1, number2))

if sel == '/':
    print(number1, '/', number2, '=', division(number1, number2))


    
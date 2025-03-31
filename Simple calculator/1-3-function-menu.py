# create functions for + - * / 

# condition for run + - * /

# show menu for calculator

def sum(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def multiplication(number1 , number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')


while True:
    # take input from the user
    choice = input('Enter choice(1/2/3/4): ')

    # check if choice is one of the four options 

    if choice in ('1', '2', '3', '4'):
        try:
            number1 = int(input('Enter first number: '))
            number2 = int(input('Enter second number: '))

        except ValueError:
            print('Invalid input. Please Enter a number.')

            continue

        if choice == '1':
            print(number1, '+', number2, '=', sum(number1, number2))

        if choice == '2':
            print(number1, '-', number2, '=', minus(number1, number2))
            
        
        if choice == '3':
            print(number1, '*', number2, '=', multiplication(number1, number2))

        
        if choice == '4':
            print(number1, '/', number2, '=', division(number1, number2))

        next_calculation = input("Let's do next calculation? (yes/no):" )

        if next_calculation == 'no':
            break
        else:
            print('Invalid Input...')


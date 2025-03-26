# Get Numbers from clients + - * /

number1 = int(input("\nPlease Enter Number One : "))

number2 = int(input("\nPlease Enter Number Two : "))

# + - * / show result for select clients 
operation = input("\nPlease Select one of the operations. \n+ \n- \n* \n/ \n: ")

# conditions for + - * /
if operation == '+':
    print(number1 + number2)

if operation == '-':
    print(number1 - number2)

if operation == '*':
    print(number1 * number2)

if operation == '/':
    print(number1 / number2)

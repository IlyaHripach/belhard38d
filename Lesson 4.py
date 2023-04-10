#1




#2
number1 = (int(input('Введите первое число - ')))
action = (input('Выберите действие +, -,  *,  / '))
number2 = (int(input('Введите второе число - ')))
otvet = ' Ответ = '
if action == '+':
    print(otvet, number1 + number2)
if action == '-':
    print(otvet, number1 - number2)
if action == '*':
    print(otvet, number1 * number2)
if action == '/':
    print(otvet, number1 / number2)
else:
     'Введите новый оператор'




#1
number = [i**2 for i in range(int(input(())))]



#2
text = input()
data = {i: text.count(i) for i in set(text)}



#3
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




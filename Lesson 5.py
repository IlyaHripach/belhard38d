#1
numbers = [i**2 for i in range(int(input(())))]

#2
text = input()
data = {i:text.count(i) for i in set(text)}

#3
n = int(input())
data1 = {
    i: {
        'name':input(f'name{i}: '),
        'email': input(f'email {i}: ')
    }
    for i in range(n)
}
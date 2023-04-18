#1
# def decimal_to_binary(decimal: int) -> str:
#     binary: str = ''
#     while decimal > 1:
#         binary = f'{decimal % 2}' + binary
#         decimal //= 2
#     binary = f'{decimal}' + binary
#     return binary.zfill(8)
# print(decimal_to_binary(15))
# print(decimal_to_binary(13))
# def binary_to_decimal(binary: str) -> int:
#     binary = binary[::-1]
#     decimal: int = 0
#     for i in range(len(binary)):
#         decimal += (2 ** i) * int(binary[i])
#         return decimal
# print(binary_to_decimal(decimal_to_binary(128)))



#2  morse asbuka



#3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 3
# numbers = numbers[-n:] + numbers[:-n]
# print(numbers)



#4
# objs = [1, 2, 3, 'hello', 4, 5, 6, 'world']
# #4.1 objs = [obj for obj in objs if isinstance(obj, str)]
# #4.2 objs = [*filter(lambda x: isinstance(x, str),objs)]
# #4.3for i in range(len(objs) -1, -1, -1)
#     if not isinstance(objs[i], str):
#         del objs[i]
# print(objs)



#5
# objs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0, len(objs) // 2):
#     objs[i], objs[~i] =  objs[~i], objs[i]
# print(objs)



#6
# numbers = [2, 3, 1, 4, 7, 8, 4, 2, 4 ,5, 7]
# odd: list = []
# even: list = []
# for number in numbers:
#     if number % 2:
#         odd.append(number)
#     else:
#         even.append(number)
# result = even + odd
# print(result)



#7
# numbers = [1, 2, 3, 4, 5]
# result = []
# for i in range(len(numbers)):
#     if i != len(numbers) -1:
#         result.append(numbers[i-1] + numbers [i+1])
#     else:
#         result.append(numbers[i -1] + numbers[0])
# print(result)



#8
# def find_country(city: str) -> str:
#     countries = {
#         'Belarus': ['Minsk', 'Gomel', 'Mogilev'],
#         'Russian': ['Moscow', 'SPB', 'Kaliningrad']
#     }
#     for country, cities in countries.items():
#         if city in cities:
#             return country



#9
# users = {
#     1:  {
#         'name': 'Alex',
#         'email': 'alex@gmail.com'
#     }
#     2: {
#         'name': 'Pavel',
#         'email': ''
#     }
#     3: {
#         'name': 'Igor',
#         'email': None
#     }
# }
# for user in users.values():
#     if not user.get('email'):
#         print(user['name'])
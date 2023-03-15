# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

# num = int(input("Введите десятичное число: "))
#
# print("0x%x" % num)
# print(f'{num:#x}')
# hex_Num = '0x'
# elem = '0123456789abcdef'
# while num > 0:
#     hex_Num = hex_Num + elem[num % 16]
#     num = num // 16
#
# print(hex_Num)

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте
# модуль fractions.

import math

frac_1 = input('Введите первую дробь вида a/b: ')
frac_2 = input('Введите вторую дробь вида a/b: ')

if frac_1.split('/')[0].isdecimal():
    a = int(frac_1.split('/')[0])
if frac_1.split('/')[1].isdecimal():
    b = int(frac_1.split('/')[1])
if frac_2.split('/')[0].isdecimal():
    c = int(frac_2.split('/')[0])
if frac_2.split('/')[1].isdecimal():
    d = int(frac_2.split('/')[1])
else:
    print('Вы ввели не верную дробь')

if b == d:
    print(f'Сумма дробей = {a + c} / {b}')
else:
    cd = int(b * d / math.gcd(b, d))
    rn = int(cd / b * a + cd / d * c)
    g2 = math.gcd(rn, cd)
    n = int(rn / g2)
    m = int(cd / g2)
    print(f'Сумма дробей = {n} / {m}' if n != m else n)

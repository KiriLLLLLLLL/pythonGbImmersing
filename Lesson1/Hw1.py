# Задание №8
# Нарисовать в консоли ёлку спросив у пользователя количество
# рядов.

# space = ' '
# stars = '*'
# b = 1
# n = int(input('Введите высоту елки: '))
# a = n -1
# for i in range(n):
#     print((space * a) + (stars * b) + (space * a))
#     b += 2
#     a -= 1


# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
# школьной тетрадке.

# for i in range(2, 10):
#     # print()
#     for j in range(2, 11):
#         print(f'{i} X {j} = {i * j}\t')
#     print()

# Как расставить блоки таблицы не додумал



# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c -
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

# a = int(input("Введите сторону а: "))
# b = int(input("Введите сторону b: "))
# c = int(input("Введите сторону c: "))
#
# if a <= b + c and b <= a + c and c <= a + b:
#     print("Это треугольник")
#     if a != b and a != c and b != c:
#         print("Разносторонний треугольник")
#     elif a == b and a == c:
#         print("Равносторонний треугольник")
#     elif a == b or a == c or b == c:
#         print("Это равнобедренный треугольник")
# else :
#     print("Такого треугольник не может существовать")




# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.Используйте
# правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.Сделайте
# ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


num = int(input("Введите число больше 0 и менее 100000: "))
counter = 0

if num < 0 or num > 100000:
    print("Вы ввели не правильное число")
else:
    for i in range(1, num):
        if num % i == 0:
            counter += 1
    if counter > 2:
        print("Число составное")
    else:
        print("Число простое")
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# import os
#
#
# def info_file(path_to: str) -> tuple:
#     path, filename = os.path.split(path_to)
#     name, ext = os.path.splitext(filename)
#     result = path, name, ext
#     return result
#
#
# find_file = info_file('C:/PycharmProjects/pythonGbImmersing/Lesson5/HW5.py')
# print(find_file)


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


# def reward(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
#     return {name: money / 100 * perc for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}
#
#
# names = ['w1', 'w2', 'w3']
# cash = [1000, 2000, 3000]
# percent = ['10.25', '20.25', '30.25']
# rew = reward(names, cash, percent)
# print(rew)

# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def fib_num(count: int) -> None:
    fib1, fib2 = 0, 1
    for i in range(count):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


count_num = int(input('How long? '))
print(list(fib_num(count_num)))

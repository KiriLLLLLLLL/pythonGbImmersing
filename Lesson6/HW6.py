# 1. Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
#
#
# __all__ = ['clues', 'play_clue']
# dict_variants = {}
#
#
# def clue(m: str, answer: list, chanse=5) -> int:
#     print(m)
#     for i in range(chanse):
#         ans = input(' Введите ответ ')
#         if ans.capitalize() in answer:
#             return i + 1
#     return 0
#
#
# def play_clue(var: dict) -> None:
#     [clue(i, j) for i, j in var.items()]
#
#
# def clues(question=None, answers=None):
#     if question is not None:
#         dict_variants[question] = answers
#     return dict_variants
#
#
# if __name__ == '__main__':
#     ques_n = 'Зимой и летом одним цветом! '
#     ans = ['Елка', 'Ель', 'Елочка']
#     clues(ques_n, ans)
#     ques_n = 'Два конца, два кольца, посередине гвоздик'
#     ans = ['Ножницы', 'Секатор', 'Пассатижы']
#     clues(ques_n, ans)
#     play_clue(clues())
#




# 2. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# __all__ = ['validate']
# from datetime import datetime
#
#
# def validate(date: str) -> bool:
#     try:
#         ref_date = datetime.strptime(date, "%d.%m.%Y").date()
#         return True
#     except:
#         return False
#
#
# def _leap_year(date: str) -> bool:
#     year = int(date.split(".")[-1])
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     date_str = input('Введите дату формата: DD.MM.YYYY  ')
#     print(validate(date_str))
#     print(_leap_year(date_str))

# 3. Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в init пакета имена модулей внутри дандер all.
# В модулях создайте дандер all и укажите только те функции, которые могут верно работать за пределами модуля.
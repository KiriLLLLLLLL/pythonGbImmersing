# Напишите функцию для транспонирования матрицы


# def transpose(arr: list) -> list:
#     new_list = zip(*arr)
#     trans_list = [list(row) for row in new_list]
#     return trans_list
#
#
# arr = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
# new_arr = transpose(arr)
#
# print(new_arr)


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def dict_add(*, arg_1, arg_2):
    args = locals()
    args = dict(reversed(item) for item in args.items())
    return args


print(dict_add(arg_1=23, arg_2='dsfgsgdf'))

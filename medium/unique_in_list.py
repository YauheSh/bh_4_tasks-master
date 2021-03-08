"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая проверит, все ли элементы в списке уникальны

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_unique([2, 1, 5, 4, 7]) -> True
is_unique([2, 1, 5, 4, 2]) -> False
"""


def is_unique(array: list) -> bool:

    for value in array:
        if array.count(value) > 1:
            result = False
        else:
            result = True

    return result


if __name__ == '__main__':
    assert is_unique([2, 1, 5, 4, 7])
    assert not is_unique([2, 1, 5, 4, 2])
    print('Решено!')

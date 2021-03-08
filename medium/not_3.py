"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая получает список с числами и возвращает список с
элементами, которые не кратны 3
"""


def not_3(array: list) -> list:

    for index, value in enumerate(array):
        if value % 3 == 0:
            array.pop(index)
        else:
            continue
    return array
    #for value in array:
    #    if value % 3 == 0:
    #        array.remove(value)
    #    else:
    #        continue
    #return array


if __name__ == '__main__':
    assert not_3([2, 1, 3, 5, 6, 4, 7]) == [2, 1, 5, 4, 7]
    print('Решено!')

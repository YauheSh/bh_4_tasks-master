"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""
from typing import Any

list_of_element = []

def odd_sum(int_list: list) -> int:
    #int_list.append(element)
    sum_list = 0
    for value in int_list:
        if isinstance(value, int) and not isinstance(value, bool):
            if value % 2 != 0:
                sum_list = sum_list + value
        else:
            raise TypeError(f"Все элементы списка должны быть целыми числами")
    return sum_list


if __name__ == '__main__':



    try:
        #print("Создаем список для обработки. Для выхода введите \'exit\'")
        #while True:
        #    element_list = input("Добавить элемент списка:")
        #    if element_list == "exit":
        #        break
        #    odd_sum(list_of_element, element_list)
        print(f"{odd_sum([0, 4, -3])}")
        """
        Для проверки можно использовать следующие списки или придумать свой
        5, -9, 4, 8, ()
        False, 5, 0
        [], 4, 7, 9
        5, 3, 8, -13, "Hi"
        """
    except TypeError as exc:
        print(f"{exc}")
    else:
        print("Код отработал без ошибок")
    finally:
        print("В любом случаи, ты старался")




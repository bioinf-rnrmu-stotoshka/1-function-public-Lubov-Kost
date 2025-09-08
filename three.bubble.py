from numbers import Number
from typing import List


def find_count_sort(n: int, numbers: List[int]) -> Number:

    """
    Функция сортировки вставками с подсчетом перестановок.
    
    Parameters
    ----------
    n : int
        Количество элементов в списке
    numbers : List[int]
        Список чисел для сортировки
    
    Returns
    -------
    Number
        Количество перестановок
    
    Raises 
    ------
    AssertionError
        n не соответствует длине списка
        numbers должен быть списком
        Длина списка не соответствует заявленному числу
        Входной параметр содержит не только числовые данные
    """
    assert isinstance(n, int) and n > 0, "n должно быть положительным целым числом"
    assert isinstance(numbers, list), "numbers должен быть списком"
    assert len(numbers) == n, "Длина списка не соответствует заявленному числу"

    s = 0
    for i in range(1, n):
        k = i
        while k >= 1 and numbers[k] < numbers[k - 1]:
            numbers[k], numbers[k - 1] = numbers[k - 1], numbers[k]
            k -= 1
            s += 1
        assert isinstance(numbers[k-1], (int, float, complex)) and not isinstance(numbers[k-1], bool), "Входной параметр содержит не только числовые данные"

    return s


count_num = 6
example_num = [6, 10, 4, 5, 1, 2]
count_sort = find_count_sort(count_num, example_num)
print(count_sort)

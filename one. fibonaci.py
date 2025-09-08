from numbers import Number

def get_fib(num_index: int) -> Number:
    """
    Функция для поиска значения фибоначи по индексу
    Parameters
    ----------
    num_index : int
        Положительное целое число до 25 включительно

    Returns
    -------
    Number
        значение числа фибоначи по его номеру (индексу)

    Raises
    ------
    AssertionError
        Входной параметр не является целым числом
        Входной параметр не положительное или больше 25
        "Факториал не определен"

    """
    assert isinstance(num_index, int), "Входной параметр не является целым числом"
    assert 0 <= num_index <= 25, "Входной параметр не положительное или больше 25"
    assert num_index >= 0, "Факториал не определен"

    if num_index == 0:
        return 0
    if num_index == 1:
        return 1
    if num_index > 1:
        return get_fib(num_index - 1) + get_fib(num_index - 2)


example_index = 23
fib_value = get_fib(example_index)
print(fib_value)

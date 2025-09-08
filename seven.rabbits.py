from numbers import Number

def bern_rabbits(n: int, k: int) -> Number:
    """
    Функция для поиска общего количества пар кроликов после n месяцев
    Parameters
    ----------
    n: int
        Косличество пройденных месяцев, число <= 40
    k: int
        Количество плодящихся пар кроликов от одной пары, число <= 5

    Returns
    -------
    Number
        Общее количество пар кроликов после n месяцев

    Raises
    ------
    AssertionError
        Входные параметры не являются целыми числами
        Входной параметр для количества месяцев больше 40
        Входной параметр для плодящихся пар больше 5
        "Факториал не определен"
    """
    assert isinstance(n, int) and isinstance(k, int), "Входные параметры не являются целыми числами"
    assert n <= 40, "Входной параметр для количества месяцев больше 40"
    assert k <= 5, "Входной параметр для плодящихся пар больше 5"
    assert n >= 1, "Факториал не определен"

    if n == 1:
        return 1
    if n == 2:
        return 1
    return bern_rabbits(n - 1,k) + bern_rabbits(n - 2,k) * k


days = 5
offspring = 3
all_rabbits = bern_rabbits(days, offspring)
print(all_rabbits)

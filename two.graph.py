from typing import List

def find_degrees(n: int, edges: List[List[int]]) -> List[int]:
    """
    Функция для вычисления степеней вершин в неориентированном графе.

    Parameters
    ----------
    n : int
        Количество вершин в графе (вершины нумеруются от 1 до n)
    edges : List[List[int]]
        Список ребер, где каждое ребро представлено парой вершин [u, v]

    Returns
    -------
    List[int]
        Массив степеней вершин, где D[i] соответствует степени вершины i+1

    Raises
    ------
    AssertionError
        Количество вершин n не является положительным целым числом
        Список edges не является списком
        Элементы edges не являются списками из двух элементов
        Вершины в ребрах выходят за допустимый диапазон [1, n]
        Вершины в ребрах не являются целыми числами
    """
    assert (isinstance(n, int) and n > 0), "Количество вершин n не является положительным целым числом"
    assert isinstance(edges, list), "Список edges не является списком"

    degrees = [0] * (n + 1)

    for edge in edges:
        assert (isinstance(edge, list) and len(edge) == 2), "Элементы edges должны быть списками из двух элементов"

        u, v = edge
        assert isinstance(u, int) and isinstance(v, int), "Вершины в ребрах должны быть целыми числами"
        assert (1 <= u <= n and 1 <= v <= n), "Вершины выходят за допустимый диапазон [1, n]"

        degrees[u] += 1
        degrees[v] += 1

    return degrees[1:]


count_vertex = 6
example_gragh = [[1, 2], [2, 3], [6, 3], [5, 6], [2, 5], [2, 4], [4, 1]]
degrees_graph = find_degrees(count_vertex, example_gragh)
print(degrees_graph)

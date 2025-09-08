from typing import Tuple

def find_count_dna(line: str) -> Tuple[int, int, int, int]:
    """
    Функция для поиска количества определенных символов в последовательности
    Parameters
    ----------
    line: str
        Строчка из нуклеотидов длиной не более 1000

    Returns
    -------
    Tuple[int, int, int, int]
        Количество каждого нуклеотида в цепочке (строчке)

    Raises
    ------
    AssertionError
        Входной параметр не является строкой
        Входной параметр является пустой строкой или содержит более 1000 символов
        Входной параметр содержит недопустимый символ
    """
    assert isinstance(line, str), "Входной параметр не является строкой"
    assert (0 < len(line) <= 1000), "Входной параметр является пустой строкой или содержит более 1000 символов"

    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for i in line:
        assert i in 'ACGT', "Входной параметр содержит недопустимый символ"
        if i == "A":
            count_a += 1
        if i == "C":
            count_c += 1
        if i == "G":
            count_g += 1
        if i == "T":
            count_t += 1

    return count_a, count_c, count_g, count_t


sequence_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_dna = find_count_dna(sequence_dna)
print(count_dna[0],count_dna[1],count_dna[2],count_dna[3])

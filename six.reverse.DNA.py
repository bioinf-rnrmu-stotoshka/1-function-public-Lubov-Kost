def reversing(line: str) -> str:
    """
    Функция для нахождения дополненной обратной последовательности ДНК
    Parameters
    ----------
    line: str
        Строчка из нуклеотидов длиной не более 1000

    Returns
    -------
    str
        Обратная дополненная ДНК

    Raises
    ------
    AssertionError
        Входной параметр не является строкой
        Входной параметр является пустой строкой или содержит более 1000 символов
        Входной параметр содержит недопустимый символ
    """
    assert isinstance(line, str), "Входной параметр не является строкой"
    assert (
        0 < len(line) <= 1000
    ), "Входной параметр является пустой строкой или содержит более 1000 символов"

    new_dna = ""
    for i in line:
        assert i in "ACGT", "Входной параметр содержит недопустимый символ"
        if i == "A":
            new_dna += "T"
        elif i == "C":
            new_dna += "G"
        elif i == "G":
            new_dna += "C"
        elif i == "T":
            new_dna += "A"

    return new_dna[::-1]


sequence_dna = "AAAACCCGGT"
reverse_dna = reversing(sequence_dna)
print(reverse_dna)

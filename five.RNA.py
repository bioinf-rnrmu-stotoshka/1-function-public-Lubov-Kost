def transcription(line: str) -> str:
    """
    Функция для транскрипции ДНК в РНК
    Parameters
    ----------
    line: str
        Строчка из нуклеотидов ДНК длиной не более 1000

    Returns
    -------
    str
        Строчка из нуклеотидов РНК с урацилом

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

    copy_dna = ""
    for i in line:
        assert i in "ACGT", "Входной параметр содержит недопустимый символ"
        if i == "T":
            copy_dna += "U"
        else:
            copy_dna += i

    return copy_dna


sequence_dna = "GATGGAACTTGACTACGTAAATT"
sequence_rna = transcription(sequence_dna)
print(sequence_rna)

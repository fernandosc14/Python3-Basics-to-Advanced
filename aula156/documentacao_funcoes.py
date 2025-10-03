""" Módulo de exemplo para demonstração de documentação de funções.

Este módulo contém funções que ilustram como documentar funções em Python
usando docstrings. Cada função inclui uma descrição, parâmetros, valor de retorno
"""

variavel_1 = 1
texto = 'texto asdasd asdasdasd asdassds'

def word_count(texto):
    """
    Conta o número de palavras em uma string.

    Args:
        texto (str): Texto a ser analisado.

    Returns:
        int: Quantidade de palavras no texto.
    """

    palavras = texto.split()
    return len(palavras)
    

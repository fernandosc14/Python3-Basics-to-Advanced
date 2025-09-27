"""
Exercicio - Unir listas
Crie uma função zipper
O trabalho dessa função será unir duas listas na ordem
Use todos os valores da menor lista
Ex:
['Lisboa', 'Madrid', 'Londres']
['Portugal', 'Espanha', 'Inglaterra', 'França']

Resultado:
[('Lisboa', 'Portugal'), ('Madrid', 'Espanha'), ('Londres', 'Inglaterra')]
"""

lista1 = ['Lisboa', 'Madrid', 'Londres']
lista2 = ['Portugal', 'Espanha', 'Inglaterra', 'França']

# def zipper(lista1, lista2):
#     return list(zip(lista1, lista2)) # zip para listas de tamanhos diferentes
#     return list(zip_longest(lista1, lista2)) # zip_longest preenche com None os valores faltantes, ou utilizar fillvalue, para valor diferente

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))

    return [
        (lista1[i], lista2[i]) for i in range(intervalo)
    ]

print(zipper(lista1, lista2))

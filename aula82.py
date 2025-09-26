"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. 
Porém, são funções anônimas que contém apenas uma linha de código.
Ou seja, tudo deve ser contido dentro de uma única expressão. 
"""

lista = [
    {'nome': 'Fernando', 'idade': 26},
    {'nome': 'Maria', 'idade': 18}, 
    {'nome': 'Helena', 'idade': 42},
    {'nome': 'Luiz', 'idade': 35},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l2 = sorted(lista, key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['idade'])

exibir(l1)
exibir(l2)

"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis.
"""
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista =  []
for num in range(10):
    lista.append(num)
# print(lista) 

lista = [
    num * 2
    for num in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] >= 20
#     else {**produto}
#     for produto in produtos
# ]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [num for num in range(10) if num < 5]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20
#     else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]
# p(novos_produtos)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
    
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x ,letra) for letra in 'Fernadno']
    for x in range(3)
]

print(lista)
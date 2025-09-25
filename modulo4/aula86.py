# Dictionary comprehension e Set comprehension
produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dict(lista))

# s1 = {i for i in range(10)}


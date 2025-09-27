from functools import partial

#map - mapear dados

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'p1', 'preco': 10.00},
    {'nome': 'p2', 'preco': 21.20},
    {'nome': 'p3', 'preco': 10.70},
    {'nome': 'p4', 'preco': 40.00},
    {'nome': 'p5', 'preco': 50.00},
]

def aumentar_percentagem(valor, percentagem):
    return round(valor * percentagem, 2)

aumentar_10 = partial(aumentar_percentagem, percentagem=1.1)

# novos_produtos = [
#     {**p,  'preco': aumentar_10(p['preco'])} 
#     for p in produtos 
# ]

def muda_preco(produto):
    return {**produto,  'preco': aumentar_10(produto['preco'])} 

novos_produtos = map(
    muda_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

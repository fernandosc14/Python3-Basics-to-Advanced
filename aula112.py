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

def filtrar_produtos(produto):
    return produto['preco'] > 10

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    filtrar_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

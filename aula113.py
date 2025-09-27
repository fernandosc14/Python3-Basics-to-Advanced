from functools import reduce

produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 22},
    {'nome': 'p3', 'preco': 2},
    {'nome': 'p4', 'preco': 6},
    {'nome': 'p5', 'preco': 4},
]

def func_reduce(acumulador, produto):
    print(acumulador, produto)
    return acumulador + produto['preco']

# total = 0
# for p in produtos:
#     total += p['preco']

total = reduce(
    func_reduce, # função
    produtos, # iterável
    0.0 # valor inicial do acumulador
)

print(total)

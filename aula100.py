import copy
import pprint

produtos = [
    {"nome": "Produto A", "preco": 10.0},
    {"nome": "Produto B", "preco": 20.0},
    {"nome": "Produto C", "preco": 15.0},
    {"nome": "Produto D", "preco": 25.0},
    {"nome": "Produto E", "preco": 30.0},
]

"""
Aumente o preço dos produtos a seguir em 10%
Gere novos_produtos por deep copy
"""

novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
     {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
     for produto in novos_produtos
]

pprint.pprint(novos_produtos)

"""
Ordene os produtos por nome descrescente
Gere produtos_ordenados_por_nome por deep copy
"""

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)

pprint.pprint(produtos_ordenados_por_nome)

"""
Ordene os produtos por preço crescente
Gere produtos_ordenados_por_preco por deep copy
"""

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco']
)

pprint.pprint(produtos_ordenados_por_preco)

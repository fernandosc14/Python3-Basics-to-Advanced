"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo chave/valor.
Chaves podem ser cosiderados como índices de uma lista.
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Muáveis: list, dict
pessoa = {
    'nome': 'Fernando',
    'apelido': 'Casas',
    'idade': 20,
    'altura': 1.72,
    'endereços': [
        {'rua': 'Av. Brasil', 'número': 320},
        {'rua': 'Av. São João', 'número': 1000}
    ]
} 
"""
# pessoa = dict(nome='Fernando')
pessoa = {
    'nome': 'Fernando',
    'apelido': 'Casas',
    'idade': 20,
    'altura': 1.72,
    'endereços': [
        {'rua': 'Av. Brasil', 'número': 320},
        {'rua': 'Av. São João', 'número': 1000}
    ],
}

# print(pessoa)
print(pessoa['nome'])
print(pessoa['apelido'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])



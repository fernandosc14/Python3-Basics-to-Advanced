"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
import copy

pessoa = {
    'nome': 'Fernando',
    'apelido': 'Casas',
    # 'idade': 900,
}

# print(len(pessoa)) # Quantas chaves
# print(list(pessoa.keys())) # Iterável com as chaves
# print(list(pessoa.values())) # Iterável com os valores
# print(list(pessoa.items())) # Iterável com chaves e valores
# pessoa.setdefault('idade', 20) # Adiciona valor se a chave não existe

# d2 = pessoa.copy() # Retorna uma cópia rasa (shallow copy)
# d2 = copy.deepcopy(pessoa) # Cópia profunda (deep copy)

# # Diferença de copy e deepcopy - se tiver um dicionário dentro de outro dicionário ou uma lista dentro de outro dicionário é necessário usar deepcopy

# print(pessoa.get('nome')) # Obtém uma chave - retorna None se não encontrar

# nome = pessoa.pop('nome') # Apaga um item com a chave especificada (del) e retorna o valor
# ultimo = pessoa.popitem() # Apaga o último item adicionado e retorna uma tupla (chave, valor)

# pessoa.update({ # Atualiza um dicionário 
#     'nome': 'João', # Se a chave existir, o valor será atualizado
#     'idade': 30, # Se a chave não existir, o par chave/valor será adicionado
# })
# pessoa.update(nome='Maria', idade=25) # Outra forma de usar o update



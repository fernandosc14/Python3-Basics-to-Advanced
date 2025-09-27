import json

# pessoa = {
#     'nome': 'Fernando',
#     'apelido': 'Casas',
#     'morada': [
#         {'rua': 'Rua A', 'cidade': 'Porto'},
#         {'rua': 'Rua B', 'cidade': 'Lisboa'}
#     ],
#     'altura': 1.75,
#     'numeros_preferidos': [3, 7, 9, 15],
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False, 
#         indent=4,
#     )

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)   

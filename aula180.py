# csv.reader e csv.DictReader
# csv.reader lê o CSV
# csv.DictReader lê o CSV e cria um dicionário com as informações

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'João', 'Idade': 30, 'Cidade': 'São Paulo'},
    {'Nome': 'Maria', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Pedro', 'Idade': 35, 'Cidade': 'Belo Horizonte'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas,
    )
    escritor.writeheader()
    
    for cliente in lista_clientes:
        escritor.writerow(cliente)

# lista_clientes = [
#     ['João', 30, 'São Paulo']
#     ['Maria', 25, 'Rio de Janeiro']
#     ['Pedro', 35, 'Belo Horizonte']
# ]

# with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
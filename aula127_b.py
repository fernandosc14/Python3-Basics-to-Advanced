"""
Exercicio - Guarde sua class em JSON
Salve os dados da sua class em JSON
e depois crie novamente as instâncias da class com os dados salvos.
"""
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

with open('aula127.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    p1  = Pessoa(**dados[0])

print(p1.__dict__)

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


p1 = Pessoa('Fernando', 32)

dados = [p1.__dict__]

with open('aula127.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)

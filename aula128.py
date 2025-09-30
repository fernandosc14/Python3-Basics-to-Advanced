"""
Métodos de class
São métodos onde 'self' será 'cls', ou seja, ao invés
de receber a instância no primeiro parâmetro, 
recebe a própria classe.
"""

class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)

p1 = Pessoa('Fernando', 20)
p2 = Pessoa.criar_50_anos('Fernando')
p3 = Pessoa.criar_anonimo(30)


print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
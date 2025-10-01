"""
Herança simples - Relações entre classes
Associação - usa, Agregação - tem
Composição - É dono de, Herança - É um

Herança ou Composição

Classe Principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (cliente)
    -> sub class, child class, derived class
"""

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido
    
    def class_name(self):
        print (self.nome, self.apelido, self.__class__.__name__)

class Cliente(Pessoa):
    def class_name(self):
        print (self.nome, self.apelido, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = '5678'


c1 = Cliente('Fernando','Casas')
c1.class_name()

c2 = Aluno('Maria','Joana')
c2.class_name()

print(c2.cpf)

# help(Cliente)
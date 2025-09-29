"""
class - Classes são modelos para criação de objetos.
As classes geram novos objetos (instâncias) que podem ter atributos e métodos.
Os objetos gerados pela classe podem ser usar os dados internos para realizar ações.
Por convenção, usamos PascalCase para nomear classes.
"""

class Pessoa:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

p1 = Pessoa('Fernando','Casas')
# p1.nome = 'Fernando'
# p1.apelido = 'Casas'

p2 = Pessoa('Fernando', 'Rocha')
# p2.nome = 'Fernando'
# p2.apelido = 'Rocha'

print(p1.nome)
print(p1.apelido)

print(p2.nome)
print(p2.apelido)

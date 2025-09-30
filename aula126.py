# Atributos de class

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Fernando', 'idade': 32}
p1 = Pessoa(**dados)

print(vars(p1))
print(p1.nome)

# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

#frozen=True -> torna a classe imutável (sem setters)
#repr=True -> cria o método __repr__() automaticamente
#eq=True -> cria o método __eq__() automaticamente
#order=True -> cria os métodos de comparação automaticamente

@dataclass(repr=True, eq=True, order=True, frozen=False)
class Pessoa:
    nome: str
    apelido: str

if __name__ == "__main__":
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista)
    print(ordenadas)
    # p1 = Pessoa('Fernando', 'Casas')
    # print(p1)

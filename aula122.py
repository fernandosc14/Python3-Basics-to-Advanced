"""
Métodos em instâncias de classes Python

Hardcoded - Escrito diretamente no código

Self - Representa a própria instância da classe - Sempre deve ser o primeiro parâmetro dos métodos
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O carro {self.nome} está acelerando.')

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)  # Mesma coisa que fusca.acelerar() - Hardcoded
# print(fusca.nome)

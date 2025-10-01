"""
Exercicios com classes
1 - Crie uma class Carro (Nome)
2 - Crie uma class Motor (Nome)
3 - Crie uma class Fabricante (Nome)
4 - Faça ligação entre Carro tem Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def info(self):
        print (f'Carro: {self.nome}, Motor: {self.motor.nome}, Fabricante: {self.fabricante.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
fusca.fabricante = Fabricante('Volkswagen')
fusca.motor = Motor('1.6')
fusca.info()

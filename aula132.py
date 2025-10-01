"""
@property + @setter - getter e setter no modo Pythônico
- como getter
- p/evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
- Atributos que começam com _ (underscore) não devem ser utilizados fora da classe
"""

class Caneta:
    def __init__(self, cor):
        # Atributo protegido
        self._cor = cor
        self._cor_tampa = None

    @property
    def color(self):
        return self._cor
    
    @color.setter
    def color(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.color = 'Vermelha'
caneta.cor_tampa = 'Azul'
print(caneta.color)
print(caneta.cor_tampa)

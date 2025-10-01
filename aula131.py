"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo do Python de fazer as coisas
@property - decorator que transforma um método em um atributo
Geralmente é utilizado nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
"""

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         print('Get cor')
#         return self.cor

    
# caneta = Caneta('Azul')
# print(caneta.get_cor())


##########################

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    @property
    def color(self):
        return self.cor

    
caneta = Caneta('Azul')
print(caneta.color)

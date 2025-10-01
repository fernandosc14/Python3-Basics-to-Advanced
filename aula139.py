"""
super() é a super class na sub classe
Classe principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (Cliente)
    -> sub class, derived class, child class
"""

# class MinhaString(str):
#     def upper(self):
#         print('Chamando upper da classe MinhaString')
#         return super().upper() 

# string = MinhaString('Geek University')
# print(string.upper())


class A:
    atributo_a = 'Valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Hey')

    def metodo(self):
        # super().metodo() # B
        # super(B, self).metodo() # A
        # super(A, self).metodo() # Object
        A.metodo(self)
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('atributo', 'Qualquer coisa')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()

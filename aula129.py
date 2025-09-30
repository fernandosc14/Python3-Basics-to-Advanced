"""
@staticmethod
Métodos estáticos são métodos que estão dentro da classe, mas não tem
acesso ao self nem ao cls.
Em resumo, são funções que existem dentro da sua classe.
"""
class Classe:

    @staticmethod
    def metodo_estatico():
        print('Método estático')

c1 = Classe()
c1.metodo_estatico()  # Método estático
Classe.metodo_estatico()  # Método estático
"""
Exercicios
Crie Funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(5))

triplicar = criar_multiplicador(3)
print(triplicar(5))

quadruplicar = criar_multiplicador(4)
print(quadruplicar(5))
"""
Exercicio - Adiando execução de funções
"""

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executa(funcao, x):
    def interna(y):
        return funcao(x, y) 
    return interna

soma_com_cnco = executa(soma, 5)
multiplica_por_10 = executa(multiplica, 10)

print(soma_com_cnco(3))          # 8
print(multiplica_por_10(3))      # 30

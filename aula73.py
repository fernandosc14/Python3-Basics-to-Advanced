"""
Higher Order Functions
Funções de primeira classe
"""

def saudar(msg, nome):
    return f'{msg}, {nome}!'

def executar (funcao, *args):
    return funcao(*args)

print(
    executar(saudar, 'Bom dia', 'Fernando')
)
print(
    executar(saudar, 'Boa noite', 'Maria')
)

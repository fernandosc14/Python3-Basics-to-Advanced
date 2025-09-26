"""
Exercicios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variavel

# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar.
"""

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variavel

def multiplica_todos(*args):
    multiplica_todos_total = 1
    for i in args:
        multiplica_todos_total *= i
        
    return multiplica_todos_total      

multiplicar = multiplica_todos(1, 2, 3, 4, 5)
print(multiplicar)
    
# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar.

def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Ímpar'

print(par_ou_impar(11))
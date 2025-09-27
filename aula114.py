"""
Funções recursivas e recursividade
- Funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores
Todas as funções recursivas devem ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
- fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

Limite de recursão
- Python tem um limite de recursão (padrão 1000)
"""
# def recursiva(inicio=0, fim=10):

#     # Caso base - Parar a recursão
#     if inicio >= fim:
#         return fim
    
#     # Caso recursivo - Contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(5))  

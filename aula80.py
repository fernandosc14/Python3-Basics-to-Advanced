"""
Sets - Conjuntos em Python (tipo set)

Representados graficamente pelo diagrama de Venn
tipos imutáveis como valor interno.

Criando um set
set(iteravel) ou {1, 2, 3}

imutável: str, int, float, bool, tupla
mutável: lista, dicionário, set

"""

# s1 = set('Fernando')
# s1 = set() # vazio
# s1 = {'Fernando', 1, 2, 3} # com dados

"""
Sets são eficientes para remover valores duplicados de iteráveis
- Os valores são únicos
- Não aceitam valores mutáveis
- Não tem indexes
- Não garantem ordem
- São iteráveis (for, in, not in)
"""
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 =set(l1)
# l2 = list(s1)

# s1 = {1, 2, 3}
# print(4 in s1)

# s1 = {1, 2, 3}
# for num in s1:
#     print(num)

"""
Métodos úteis:
add, update, clear, discard
"""

# s1 = set()
# s1.add('Fernando')
# s1.add(1)
# s1.update(('Olá',)) # pode passar lista, tupla, dicionário, set | * terminar com vírgula
# # s1.clear() # limpa o set
# s1.discard('Fernando') # remove o valor do set
# print(s1)

"""
Operadores úteis:
união | união (union) - Une
interseção & interseção (intersection) - Itens em comum
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2 # União
# s4 = s1 & s2 # Interseção
# s5 = s1 - s2 # Diferença (presente no set da esquerda)
# s6 = s1 ^ s2 # Diferença simétrica (itens que não estão em ambos)

# Exemplo práticos

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Letra "l" encontrada')
        break



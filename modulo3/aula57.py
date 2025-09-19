"""
Lista de listas e indices
"""

salas = [
    ['Maria', 'Helena'], # 0

    ['Elaine'], # 1

    ['Luiz', 'João', 'Eduardo'], # 2
]

# print(salas) #[['Maria', 'Helena'], ['Elaine'], ['Luiz', 'Jo�o', 'Eduardo']]
# print(salas[0]) #['Maria', 'Helena']
# print(salas[0][1]) #Helena
# print(salas[2][1]) #João
# etc...


for sala in salas:
    print('A sala é:', sala)
    for aluno in sala:
        print(aluno)
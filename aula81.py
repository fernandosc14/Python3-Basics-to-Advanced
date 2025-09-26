"""
Exercício
Crie uma função que encontre o primeiro duplicado considerando o segundo número como a duplicação.
Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número duplicado em si.
    Exemplo: 
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros= [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # -1
    [1, 1, 3, 4, 2, 3, 7, 8, 9, 0], # 1
    [1, 5, 6, 7, 5, 1, 6, 9, 0], # 5
]

def encontra_duplicado(lista):
    numeros_checados = set()
    primeiro_duplicado = -1

    for num in lista:
        if num in numeros_checados:
            primeiro_duplicado = num
            break
        
        numeros_checados.add(num)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_duplicado(lista)
    )
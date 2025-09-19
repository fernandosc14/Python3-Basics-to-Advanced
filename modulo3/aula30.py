"""
# - Exercício 1 -
try:
    n1 = int(input("Digite o primeiro número: "))
    if n1 % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except:
    print("Não inseriu um número inteiro")   


# - Exercício 2 -
try:
    hora = int(input("Insira a hora: "))

    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida")
except:
    print("Não inseriu um número inteiro")
"""
# - Exercício 3 -

try:
    nome = input("Digite seu nome: ")

    if len(nome) <= 4:
        print("Seu nome é curto")
    elif len(nome) >= 5 and len(nome) <= 6:
        print("Seu nome é normal")
    elif len(nome) >= 7:
        print("Seu nome é grande")
    else:
        print("Nome inválido")
except:
    print("Nome inválido")
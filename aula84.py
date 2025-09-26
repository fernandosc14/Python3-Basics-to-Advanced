# Empacotamente e Desempacotamento de dicionários


# a, b = 1, 2
# a, b = b, a
# print(a, b)

#===================

# pessoa = {
#     'nome': 'Fernando',
#     'apelido': 'Casas'
# }
# (a1 ,a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Fernando',
    'apelido': 'Casas'
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.70
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Argumentos não nomeados: ',args)
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

# mostro_argumentos_nomeados(nome='Fernando', idade=20, altura=1.70)
# mostro_argumentos_nomeados(**pessoas_completa)

configuration = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'arg5': 5,
}

mostro_argumentos_nomeados(**configuration)

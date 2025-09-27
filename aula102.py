# Variáveis livres + nonlocal

# def fora(x):
#     a = x

#     def dentro():
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
final = c('c')
print(final)

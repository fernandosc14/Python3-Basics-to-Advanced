"""
Valores Truthy e Falsy, tipos mutáveis e imutáveis
Mutáveis [] {} set()
Imutáveis () '' 0 0.0 None False range(0, 10)
"""
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(falsy(lista))
print(falsy(dicionario))
print(falsy(conjunto))
print(falsy(tupla))
print(falsy(string))
print(falsy(inteiro))
print(falsy(flutuante))
print(falsy(nada))
print(falsy(falso))
print(falsy(intervalo))
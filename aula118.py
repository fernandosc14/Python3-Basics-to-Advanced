# Problema dos params mutáveis em funções python
def adiciona_elemento(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_elemento('Maria')
adiciona_elemento('João', cliente1)
adiciona_elemento('Fernando', cliente1)
cliente1.append('Luiza')

cliente2 = adiciona_elemento('Ana')
adiciona_elemento('Pedro', cliente2)

cliente3 = adiciona_elemento('Ana')
adiciona_elemento('Jonny', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

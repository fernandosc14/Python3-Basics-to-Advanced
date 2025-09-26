lista_a = [1, 2, 3, 4, 5]

#lista_b = lista_a.copy() # -> Cria uma cópia da lista
lista_b = lista_a # -> Cria uma referência à lista

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

for e in lista_a:
    print(e)
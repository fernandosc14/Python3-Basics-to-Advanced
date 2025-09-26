"""
Listas:
    CRUD {CREATE, READ, UPDATE, DELETE}
    Metodos: Append, insert, pop, del, clear, extend, ....
"""

#lista = [10, 20, 30, 40]
#lista.append(50)
#lista.pop()
#lista.insert(2, 25)
#del lista[3]
#print(lista)

lista_a = [10, 20, 30, 40]
lista_b = [50, 60, 70, 80]

lista_c = lista_a + lista_b # Concatena lista_a e lista_b

lista_a.extend(lista_b) # Adiciona os elementos de lista_b ao final de lista_a
print(lista_a)
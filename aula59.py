# Desempacotamento em chamadas
# de métodos e funções

string = 'Python'
lista = [1, 2, 3]
tupla = 'a', 'b', 'c'

# a, b, c, *_ = lista # *_ => ignorar o resto 
# print(a, c)

print(*lista,) # desempacotamento
print(*string)
print(*tupla)

# Um iterável é um objeto capaz de retornar seus elementos um por vez, permitindo que seja percorrido em um loop (como for).
# Exemplos de iteráveis: str, list, tuple, set, dict.
# Objetos não iteráveis, como int, float e bool, não podem ser percorridos dessa forma.

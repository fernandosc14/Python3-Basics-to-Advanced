# raise - Lança uma exceção

def dividir(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero')
    return n1 / n2

print(dividir(8, 2))
print(dividir(8, 0))  # Vai lançar a exceção ValueError
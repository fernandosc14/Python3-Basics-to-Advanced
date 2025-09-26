"""
Introdução às generator functions em python
generator = (n for n in range(10000))
"""

def generator(n=0):
    yield 1 # Pausa aqui e retoma na próxima iteração
    return 'Acabou'

gen = generator()
print(next(gen))

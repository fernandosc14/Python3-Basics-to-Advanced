"""
Valores padrão para parâmetros
Ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
utilizado.
Refatorar: editar código.
"""

def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(x + y)

# soma (1,2)
# soma (3,4)
soma (100,200, 0)
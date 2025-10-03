# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    raise exception_

try:
    levantar()
except MyError as e:
    print(e)
    exception_ = MyError('VOU LANÇAR OUTRA')
    raise exception_ from e

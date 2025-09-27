"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Modificar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções
Decoradores são "Syntax Sugar"
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou executar a função interna')
        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)

        return resultado
    return interna

@criar_funcao # Decorator Syntax Sugar
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)


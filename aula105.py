"""
Decoradores com params
"""
def fabrica_de_decoradores(a=None,b=None,c=None):
    def decorador(func):
        print('Decorador executado')

        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return decorador

@fabrica_de_decoradores(1,2,3)
def soma(x, y):
    return x + y

decorador = fabrica_de_decoradores()
multiplica = decorador(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vez_cinco = multiplica(10, 5)

print(dez_mais_cinco)
print(dez_vez_cinco)

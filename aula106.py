def params_decorador(nome):
    def decorador(func):
        print('Decorador executado', nome)

        def nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return nova_funcao
    return decorador

@params_decorador('segundo')
@params_decorador('primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

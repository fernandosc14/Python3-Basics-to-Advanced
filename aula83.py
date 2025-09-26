def executa(funcao, *args):
    return funcao(*args)

def cria_multiplicados(multiplicador):
    def multiplica(num):
        return num * multiplicador
    return multiplica

print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)

duplica = executa(
        lambda m : lambda n: n * m,
        2
    )

print(
   duplica(5) 
)

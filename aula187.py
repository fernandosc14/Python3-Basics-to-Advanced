# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code

import sys

argumentos = sys.argv
qtd = len(argumentos)

if qtd <= 1:
    print('Não foram passados argumentos')
else:
    print(f'Foram passados {format(qtd - 1)} argumentos')
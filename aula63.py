"""
Calculo do segundo digito do CPF
CPF: 746.824.890.70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada digito por uma contagem regressiva começando em 11.

Ex.: 746.824.890-70 (746824890)
    11 10 9  8  7  6  5  4  3  2
    7  4  6  8  2  4  8  9  0  7 <- primeiro digito
    77 40 54 64 14 24 40 36 0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0

Se o resultado anterior for maior que 9:
    o digito é 0
caso contrário:
    é o próprio resultado.

O primeiro digito do CPF é 7
"""
import re # Regular Expression - Expressão Regular

cpf = '057.091.570-82'

# cpf = cpf.replace('.','').replace('-','').replace(' ','') # -> Alternativa 
"""
 * Substitui algo em uma string por outra coisa
"""
cpf = re.sub( 
    r'[^0-9]', # expressao regular para pegar tudo que não for número
    '', # com o que vai substituir
    cpf # string onde vai fazer a substituição do
)

first9 = cpf[:9]

soma = 0
multi = 10

for num in first9:
    soma += int(num) * multi
    multi -= 1

first_digit = soma * 10 % 11

"""
=> Agora o segundo num
"""

first10 = cpf[:9] + str(first_digit)

soma = 0
multi = 11

for num in first10:
    soma += int(num) * multi
    multi -= 1

second_digit = soma * 10 % 11

cpf_gerado = f'{first9}{first_digit}{second_digit}'

if cpf_gerado == cpf:
    print(f'CPF VÁLIDO: {cpf_gerado}')
else:
    print('CPF INVÁLIDO')

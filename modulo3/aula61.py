"""
CPF: 746.824.890.70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada digito por uma contagem regressiva começando em 10.

Ex.: 746.824.890-70 (746824890)
    10 9  8  7  6  5  4  3  2
    7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    o digito é 0
caso contrário:
    é o próprio resultado.

O primeiro digito do CPF é 7
"""

cpf = '746.824.890-70'

cpf = cpf.replace('.','').replace('-','')

first9 = cpf[:9]

soma = 0
multi = 10

for num in first9:
    soma += int(num) * multi
    multi -= 1

final_result = soma * 10 % 11

print("O primeiro digito do CPF é",final_result if final_result <= 9 else 0)

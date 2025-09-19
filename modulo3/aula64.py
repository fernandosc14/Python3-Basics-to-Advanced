import random

first9 = ''
for i in range(9):
    first9 += str(random.randint(0, 9))

soma = 0
multi = 10

for num in first9:
    soma += int(num) * multi
    multi -= 1

first_digit = soma * 10 % 11

"""
=> Agora o segundo num
"""

first10 = first9 + str(first_digit)

soma = 0
multi = 11

for num in first10:
    soma += int(num) * multi
    multi -= 1

second_digit = soma * 10 % 11

cpf_gerado = f'{first9}{first_digit}{second_digit}'

print(cpf_gerado)
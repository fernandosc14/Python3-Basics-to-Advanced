# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

total = 1_000_000

data_inicio = datetime(2020, 12, 20)
delta = relativedelta(years=5)
data_final = data_inicio + delta

datas = []
data_parcela = data_inicio

while data_parcela < data_final:
    datas.append(data_parcela)
    data_parcela += relativedelta(months=1)

num_parcelas = len(datas)
valor_parcelas = total / num_parcelas

for data in datas:
    print(data.strftime('%d/%m/%Y'), f'{valor_parcelas:,.2f} €')

print()

print(f'Tem {total:,.2f} € para pagar em '
      f'{delta.years} anos'
      f' ({num_parcelas} meses) em parcelas de'
      f' {valor_parcelas:,.2f} € cada.'
      )

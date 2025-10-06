# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

# date = datetime.now(timezone('Europe/Lisbon'))
date = datetime.now()
# print(date.timestamp())
print(datetime.fromtimestamp(1759763759))

# date_str_date = '2025-10-06 15:58:45'
# date_str = '06/10/2025'
# data_str_format = '%d/%m/%Y'

# date = datetime(2025, 10, 6, tzinfo=timezone('America/Sao_Paulo'))
# date = datetime.strptime(date_str, data_str_format)

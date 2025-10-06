# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('01/01/2023 12:00:00', fmt)
data_fim = datetime.strptime('31/12/2023 12:00:00', fmt)
print(data_fim)

# print(data_fim > data_inicio)  # True
# print(data_fim < data_inicio)  # False
# print(data_fim - data_inicio) # Timedelta

delta = timedelta(days=10)
# print(data_fim + delta) # 10 dias depois
print(data_fim + relativedelta(seconds=60))

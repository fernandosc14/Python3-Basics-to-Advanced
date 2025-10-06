from datetime import datetime

fmt = '%d/%m/%Y'

date = datetime.strptime('2025-10-06', '%Y-%m-%d')
print(date.strftime('%d'))

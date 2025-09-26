# Try, except, else e finally
try:
    print('Abri um arquivo')
    8 / 0
except ZeroDivisionError:
    print('Dividi por zero')
else:
    print('Não deu erro')
finally:
    print('Fechei o arquivo')
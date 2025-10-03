"""
Método especial __call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma class "callable"
"""

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(f'{name} está a ligar para {self.phone}...')


call1 = CallMe('1234-5678')
call1('Fernando')

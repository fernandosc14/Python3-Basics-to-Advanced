# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (Overload)
# Sobreposição de métodos (Override)

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando email com a mensagem: {self.mensagem}')
        return True

class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando sms com a mensagem: {self.mensagem}')
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso')
    else:
        print('Falha ao enviar notificação')

notificar(NotificacaoEmail('Olá, tudo bem?'))
notificar(NotificacaoSms('Olá, tudo bem?'))

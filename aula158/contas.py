from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: str, numero:int, saldo:float) -> None:
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    def depositar(self, valor: float):
        self._saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self._saldo}")
    
    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero: int, saldo: float, limite: float):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            print("Saldo insuficiente")
            return
        self._saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self._saldo}")
    

class ContaPoupanca(Conta):
    def __init__(self, agencia: str, numero: int, saldo: float):
        super().__init__(agencia, numero, saldo)
    
    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            print("Saldo insuficiente")
            return
        self._saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self._saldo}")
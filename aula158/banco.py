class Banco:
    def __init__(self, nome):
        self._nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)
    
    def autenticar(self, cliente):
        if cliente not in self.clientes:
            print("Cliente não pertence ao banco")
            return False
        if cliente.conta not in self.contas:
            print("Conta não pertence ao banco")
            return False
        if cliente.conta.agencia != self._nome:
            print("Agência não pertence ao banco")
            return False
        return True
    
    def sacar(self, cliente, valor):
        if self.autenticar(cliente):
            cliente.conta.sacar(valor)
        else:
            print("Autenticação falhou. Saque não realizado.")
    
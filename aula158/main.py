"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from pessoas import Pessoa, Cliente
from contas import ContaCorrente, ContaPoupanca
from banco import Banco


if __name__ == "__main__":
    conta_corrente = ContaCorrente("001", "1234-5", 1000, 500) # Description: Conta corrente com limite de 500
    cliente1 = Cliente("João", 30, conta_corrente) # Description: Cliente João com conta corrente

    banco = Banco("001") # Description: Banco com agência 001
    banco.adicionar_cliente(cliente1) # Description: Adiciona cliente ao banco

    banco.sacar(cliente1, 200) # Description: Saque de 200
    banco.sacar(cliente1, 900) # Description: Saque de 900, deve falhar por saldo insuficiente
    banco.sacar(cliente1, 500) # Description: Saque de 500, deve ser bem sucedido


    conta_poupanca = ContaPoupanca("001", "5432-1", 1500) # Description: Conta poupança
    cliente2 = Cliente("Maria", 25, conta_poupanca) # Description: Cliente Maria com conta poupança

    banco.adicionar_cliente(cliente2) # Description: Adiciona cliente ao banco

    banco.sacar(cliente2, 2000) # Description: Saque de 2000, deve falhar por saldo insuficiente
    banco.sacar(cliente2, 1000) # Description: Saque de 1000, deve ser bem sucedido
    banco.sacar(Cliente("Pedro", 40, conta_corrente), 100) # Description: Cliente não pertence ao banco, saque não realizado
        
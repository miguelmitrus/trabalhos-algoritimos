class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado.")

    def sacar(self, valor):

        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado.")

        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print("Saldo atual:", self.saldo)


conta = ContaBancaria(1000)

conta.exibir_saldo()

conta.depositar(500)

conta.exibir_saldo()

conta.sacar(300)

conta.exibir_saldo()

conta.sacar(2000)

conta.exibir_saldo()
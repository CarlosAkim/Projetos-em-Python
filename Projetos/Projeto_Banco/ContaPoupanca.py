from Conta import Conta


class ContaPoupanca(Conta):

  def __init__(self, agencia, conta, saldo=0):
    super().__init__(agencia, conta, saldo)

  def sacar(self, valor):
    if (self.saldo - valor <= 0):
      print("Saque indisponivel, por falta de saldo")
    else:
      self.saldo -= valor

  def deposito(self, valor):
    super().deposito(valor)

  def info(self):
    super().info()

  def __str__(self):
    return super().__str__()
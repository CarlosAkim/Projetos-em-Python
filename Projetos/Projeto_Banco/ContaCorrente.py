from Conta import Conta


class ContaCorrente(Conta):

  def __init__(self, agencia, conta, saldo=0):
    super().__init__(agencia, conta, saldo)

  def sacar(self, valor):
    if valor > self.saldo:
      print("Saque recusado, valor acima do saldo")
    else:
      self.verificaLimite(valor)
      super()
      print("Valor retirado com sucesso")

  def deposito(self, valor: int):
    super().deposito(valor)

  def verificaLimite(self, valor):
    limite = -200
    if valor > limite and self.saldo < -200:
      print("Valor estourou o limite")
    else:
      self.saldo -= valor
      return

  def info(self):
    super().info()

  def __str__(self):
    return super().__str__()

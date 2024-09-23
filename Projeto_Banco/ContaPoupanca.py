from Conta import Conta

class ContaPoupanca(Conta):

  def __init__(self, agencia: int, conta: int, saldo=0):
    # Inicializa a conta poupança chamando o construtor da superclasse (Conta).
    super().__init__(agencia, conta, saldo)

  def sacar(self, valor: int) -> None:
    # Sobrescreve o método de saque. Verifica se o saldo após o saque será negativo.
    # Se for, imprime uma mensagem de saldo insuficiente. Caso contrário, realiza o saque.
    if (self.saldo - valor <= 0):
      print("Saque indisponível, por falta de saldo")
    else:
      self.saldo -= valor

  def deposito(self, valor: int) -> None:
    # Sobrescreve o método de depósito. Chama o método de depósito da superclasse.
    super().deposito(valor)

  def info(self) -> None:
    # Sobrescreve o método de informação. Chama o método de info da superclasse.
    super().info()

  def __str__(self) -> str:
    # Sobrescreve o método especial de string. Chama o método __str__ da superclasse.
    return super().__str__()

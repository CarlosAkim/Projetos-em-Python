from Conta import Conta

class ContaCorrente(Conta):

  def __init__(self, agencia: int, conta: int, saldo=0):
    # Inicializa a conta corrente chamando o construtor da superclasse (Conta).
    super().__init__(agencia, conta, saldo)

  def sacar(self, valor: int) -> None:
    # Sobrescreve o método de saque. Verifica se o valor do saque é maior que o saldo.
    # Se for, recusa o saque. Caso contrário, verifica o limite e realiza o saque.
    if valor > self.saldo:
      print("Saque recusado, valor acima do saldo")
    else:
      self.verificaLimite(valor)
      super().sacar(valor)
      print("Valor retirado com sucesso")

  def deposito(self, valor: int) -> None:
    # Sobrescreve o método de depósito. Chama o método de depósito da superclasse.
    super().deposito(valor)

  def verificaLimite(self, valor: int) -> None:
    # Verifica se o valor do saque ultrapassa o limite permitido.
    # Se o saldo for maior que o limite (-200), imprime uma mensagem de erro.
    # Caso contrário, subtrai o valor do saldo.
    limite = -200
    if self.saldo - valor > limite:
      print("Valor estourou o limite")
    else:
      self.saldo -= valor

  def info(self) -> None:
    # Sobrescreve o método de informação. Chama o método de info da superclasse.
    super().info()

  def __str__(self) -> str:
    # Sobrescreve o método especial de string. Chama o método __str__ da superclasse.
    return super().__str__()

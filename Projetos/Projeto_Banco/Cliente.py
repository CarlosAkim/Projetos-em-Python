from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Pessoa import Pessoa


class Cliente(Pessoa):

  def __init__(self, nome: str, idade: int):
    super().__init__(nome, idade)
    self.conta: ContaCorrente | ContaPoupanca | None = None

  def adicionarContaCorrente(self, **kwargs: int):
    if self.conta is None:
      self.conta = ContaCorrente(**kwargs)
    else:
      raise Exception("Valor já atribuido a conta")

  def adicionarContaSalario(self, **kwargs):
    if self.conta is None:
      self.conta = ContaPoupanca(**kwargs)
    else:
      raise Exception("Valor já atribuido a conta")

  def __str__(self):
    return super().__str__()

  def deposito(self, valor: int):
    self.conta.deposito(valor)

  def sacar(self, valor: int):
    self.conta.sacar(valor)

  def info(self):
    super().info()
    self.conta.info()

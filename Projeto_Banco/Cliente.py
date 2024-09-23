from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Pessoa import Pessoa


class Cliente(Pessoa):

  def __init__(self, nome: str, idade: int):
    # Inicializa o cliente com nome e idade, chamando o construtor da superclasse (Pessoa).
    super().__init__(nome, idade)
    # Inicializa o atributo conta como None. O cliente pode ter uma ContaCorrente ou ContaPoupanca.
    self.conta: ContaCorrente | ContaPoupanca | None = None

  def adicionarContaCorrente(self, **kwargs: int):
    # Adiciona uma conta corrente ao cliente, se o cliente ainda não tiver uma conta.
    # Lança uma exceção se o cliente já tiver uma conta.
    if self.conta is None:
      self.conta = ContaCorrente(**kwargs)
    else:
      raise Exception("Valor já atribuído a conta")

  def adicionarContaSalario(self, **kwargs: int):
    # Adiciona uma conta poupança ao cliente, se o cliente ainda não tiver uma conta.
    # Lança uma exceção se o cliente já tiver uma conta.
    if self.conta is None:
      self.conta = ContaPoupanca(**kwargs)
    else:
      raise Exception("Valor já atribuído a conta")

  def __str__(self):
    # Sobrescreve o método especial de string. Chama o método __str__ da superclasse.
    return super().__str__()

  def deposito(self, valor: int) -> None:
    # Realiza um depósito na conta do cliente, se o cliente tiver uma conta.
    # Lança uma exceção se o cliente não tiver uma conta.
    if self.conta is not None:
      self.conta.deposito(valor)
    else:
      raise Exception("Conta não existente")

  def sacar(self, valor: int) -> None:
    # Realiza um saque na conta do cliente, se o cliente tiver uma conta.
    # Lança uma exceção se o cliente não tiver uma conta.
    if self.conta is not None:
      self.conta.sacar(valor)
    else:
      raise Exception("Conta não existente")

  def info(self) -> None:
    # Exibe as informações do cliente chamando o método info da superclasse.
    # Se o cliente tiver uma conta, exibe as informações da conta também.
    super().info()
    if self.conta is not None:
      self.conta.info()
    else:
      print("Cliente não possui conta bancária")

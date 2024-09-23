from abc import ABC, abstractmethod

class Conta(ABC):

  def __init__(self, agencia: int | None = None, conta: int | None = None, saldo: int = 0):
    # Inicializa a conta com a agência, número da conta e saldo.
    # Os valores padrão são None para agência e conta, e 0 para saldo.
    self.agencia: int | None = agencia 
    self._conta: int | None = conta 
    self.saldo: int = saldo

  @abstractmethod
  def sacar(self, valor: int) -> None:
    # Método abstrato para saque. Reduz o saldo pelo valor especificado.
    # Deve ser implementado por subclasses.
    self.saldo -= valor

  @abstractmethod
  def deposito(self, valor: int) -> None:
    # Método abstrato para depósito. Aumenta o saldo pelo valor especificado.
    # Deve ser implementado por subclasses.
    self.saldo += valor

  @property
  def conta(self) -> int | None:
    # Getter para o número da conta.
    return self._conta

  @abstractmethod
  def info(self) -> None:
    # Método abstrato para imprimir informações da conta.
    # Deve ser implementado por subclasses.
    print(f"Agencia: {self.agencia}")
    print(f"Conta: {self._conta}")
    print(f"Saldo: {self.saldo}")

  def __str__(self) -> str:
    # Método especial para representar a conta como string.
    # Retorna uma string formatada com a agência, número da conta e saldo.
    return f'{self.agencia}, {self._conta}, {self.saldo}'

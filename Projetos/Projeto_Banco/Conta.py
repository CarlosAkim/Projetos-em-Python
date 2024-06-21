from abc import ABC, abstractmethod


class Conta(ABC):

  def __init__(self, 
               agencia : int | None =None, 
               conta: int | None =None, 
               saldo=0):
    self.agencia = agencia
    self._conta = conta
    self.saldo = saldo

  @abstractmethod
  def sacar(self, valor: int):
    self.saldo -= valor

  @abstractmethod
  def deposito(self, valor : int):
    self.saldo += valor

  @property
  def conta(self):
    return self._conta

  @abstractmethod
  def info(self) -> None:
    print(f"Agencia: {self.agencia}")
    print(f"Conta: {self._conta}")
    print(f"Saldo: {self.saldo}")

  def __str__(self):
    return (f'{self.agencia}, {self._conta}, {self.saldo}')

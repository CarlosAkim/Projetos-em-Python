from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
import Conta


class Banco:

  def __init__(self, nome: str, contas: list[Conta.Conta] | None,
               clientes: list[Cliente] | None):
    self.nome = nome
    self.contas = contas or []
    self.clientes = clientes or []

  def acrescentarCliente(self, cliente: Cliente):
    if cliente is not None:
      self.clientes.append(cliente)

  def acrescentarConta(self, conta: ContaCorrente | ContaPoupanca | None):
    if conta is not None:
      self.contas.append(conta)
    else:
      raise ValueError("O valor não pode ser None")

  def auth(self, cliente: Cliente, conta: ContaCorrente | ContaPoupanca | None,
           valor: int):
    if cliente in self.clientes and conta in self.contas:
      cliente.sacar(valor)
    else:
      raise Exception("Não liberado saque")

  def sacar(self, cliente: Cliente,
            conta: ContaCorrente | ContaPoupanca | None, valor: int):
    self.auth(cliente, conta, valor)

from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
import Conta


class Banco:

  def __init__(self, 
               nome: str, contas: list[Conta.Conta] | None= None, 
               clientes: list[Cliente] | None= None):
    # Inicializa o banco com um nome, uma lista de contas e uma lista de clientes.
    # Se contas ou clientes não forem fornecidos, inicializa como listas vazias.
    self.nome: str = nome
    self.contas: list[Conta.Conta] = contas or []
    self.clientes: list[Cliente] = clientes or []

  def acrescentarCliente(self, cliente: Cliente):
    # Adiciona um cliente à lista de clientes, se o cliente não for None.
    if cliente is not None:
      self.clientes.append(cliente)

  def acrescentarConta(self, conta: ContaCorrente | ContaPoupanca | None):
    # Adiciona uma conta à lista de contas, se a conta não for None.
    # Caso contrário, levanta um ValueError.
    if conta is not None:
      self.contas.append(conta)
    else:
      raise ValueError("O valor não pode ser None")

  def auth(self, cliente: Cliente, conta: ContaCorrente | ContaPoupanca | None, valor: int):
    # Verifica se o cliente e a conta estão registrados no banco.
    # Se ambos estiverem registrados, permite o saque.
    # Caso contrário, levanta uma exceção.
    if cliente in self.clientes and conta in self.contas:
      cliente.sacar(valor)
    else:
      raise Exception("Não liberado saque")

  def sacar(self, cliente: Cliente, conta: ContaCorrente | ContaPoupanca | None, valor: int):
    # Tenta realizar o saque chamando o método de autenticação.
    # Se a autenticação for bem-sucedida, o saque é realizado.
    self.auth(cliente, conta, valor)

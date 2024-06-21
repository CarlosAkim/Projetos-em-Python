"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from Cliente import Cliente
from Banco import Banco

cliente1 = Cliente("Carlos", 29)
cliente2 = Cliente("Lavinia", 1)

cliente1.adicionarContaCorrente(agencia=1234, conta=6424)

cliente2.adicionarContaSalario(agencia=3241, conta=6424)

cliente2.deposito(250)

# cliente2.info()

print(10 * "-")
cliente1.deposito(1500)

# cliente1.info()

itau = Banco("Itau")

itau.acrescentarCliente(cliente1)
itau.acrescentarCliente(cliente2)
itau.acrescentarConta(cliente1.conta)

itau.acrescentarConta(cliente2.conta)

itau.clientes[0].info()

itau.sacar(cliente1, cliente1.conta, 295)

print(10 * "-")

itau.clientes[0].info()

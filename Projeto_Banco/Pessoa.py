from abc import ABC, abstractmethod


class Pessoa(ABC):

  def __init__(self, nome: str, idade: int):
    # Inicializa a pessoa com nome e idade.
    self._nome: str = nome
    self._idade: int = idade

  @property
  def nome(self) -> str:
    # Retorna o nome da pessoa.
    return self._nome

  @property
  def idade(self) -> int:
    # Retorna a idade da pessoa.
    return self._idade

  def __str__(self) -> str:
    # Retorna uma string formatada com o nome e idade da pessoa.
    return f'{self._nome} {self._idade}'

  @abstractmethod
  def info(self) -> None:
    # Método abstrato para exibir informações da pessoa.
    # Deve ser implementado por subclasses.
    print(f"Nome: {self._nome}")
    print(f"Idade: {self._idade}")

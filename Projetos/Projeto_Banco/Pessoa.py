from abc import ABC, abstractmethod


class Pessoa(ABC):

  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade

  @property
  def nome(self):
    return self._nome

  @property
  def idade(self):
    return self._idade

  def __str__(self) -> str:
    return (f'{self._nome} {self._idade}')

  @abstractmethod
  def info(self):
    print(f"Nome: {self._nome}")
    print(f"Idade: {self._idade}")

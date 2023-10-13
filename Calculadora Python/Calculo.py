print('Calculadora em Python')
while True:
  try:
    primeiroNumero = int(input('primeiro digite o valor: '))
    operador = (input('Digite o operador ( + , - , / , * ): '))
    segundoNumero = int(input('Agora digite o segundo valor: '))
  except ValueError:
    print('Ops, valor digitado não é um numero')
    continue

  if operador == '+':
    resultado = primeiroNumero + segundoNumero
    print(f'Resultado de {primeiroNumero} {operador} {segundoNumero} = {resultado}')
    break
  elif operador == '-':
    resultado = primeiroNumero - segundoNumero
    print(f'Resultado de {primeiroNumero} {operador} {segundoNumero} = {resultado}')
    break
  elif operador == '/':
    resultado = primeiroNumero / segundoNumero
    print(f'Resultado de {primeiroNumero} {operador} {segundoNumero} = {resultado}')
    break
  elif operador == '*':
    resultado = primeiroNumero * segundoNumero
    print(f'Resultado de {primeiroNumero} {operador} {segundoNumero} = {resultado}')
    break
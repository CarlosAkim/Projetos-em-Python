z = int(input('Digite um valor: '))

def conta100(value):
  cont100 =0

  for b in range(99, value, 100):
    cont100 = cont100 + 1
    soma100 = value - (cont100*100)

  print(f'Você está recebendo {cont100} notas de R$100')
  if (soma100 <= 19):
    print(f'Ficou pendente o valor de R${soma100} em sua conta, pois não temos nota abaixo de R$20,00')
  else:
    return (soma100)

def conta50(value):
  cont50 = 0

  for x in range(49, value, 50):
    cont50 = cont50 + 1
    soma50 = value - (cont50*50)

  print(f'Você está recebendo {cont50} notas de R$50')
  if (soma50 <= 19):
    print(f'Ficou pendente o valor de R${soma50} em sua conta, pois não temos nota abaixo de R$20,00')
  else:
    return (soma50)


def conta20(value):
  cont20 = 0

  for x in range(19, value, 20):
    cont20 = cont20 + 1
    soma20 = value - (cont20*20)

  print(f'Você está recebendo {cont20} notas de R$20')
  print(f'Ficou pendente o valor de R${soma20} em sua conta, pois não temos nota abaixo de R$20,00')
  return (soma20)


try:
  if z >= 100:
    sobra100 = conta100(z)
    if sobra100 < 99 and sobra100 >  50:
      sobra50 = conta50(sobra100)

      if sobra50 >=20:
        conta20(sobra50)

    if sobra100 <= 49 and sobra100 >= 20:
      conta20(sobra100)

  if z <=99 and z >= 50:
    sobra50 = conta50(z)

    if sobra50 > 20:
      conta20(sobra50)

  if z <= 49 and z >= 20:
      conta20(z)
except TypeError:
  print('')

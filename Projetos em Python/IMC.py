def calculoPeso():
  while True:
    try:
      peso = float(input('Digite o seu peso (Kg): '))
    except ValueError:
      print('Ops, valor digitado não é um numero')
      continue
    else:
      return peso
      break

def calculoAltura():
  while True:
    try:
      altura = float(input('Digite a sua altura (metros): '))
      altura2 = pow(altura,2)
    except ValueError:
      print('Ops, tivemos algum erro ai, verifica e tenta novamente')
      continue
    else:
      return round(altura2,2)
      break

def calculoIMC(peso,altura):
  imc = peso / altura
  return imc

print('Olá, vamos medir o seu IMC, por favor siga as instruções a seguir.')
peso = calculoPeso()
altura = calculoAltura()
imc = calculoIMC(peso, altura)

if imc > 40 :
  print(f'Seu IMC é de {imc:.2f}, Obesidade Mórbida (grau III)')

if imc >= 35 and imc < 39.9:
  print(f'Seu IMC é de {imc:.2f}, Obesidade Severa (grau II)')

if imc >= 30 and imc < 34.9:
  print(f'Seu IMC é de {imc:.2f}, Obesidade Leve (grau I)')

if imc >= 25 and imc < 29.9:
  print(f'Seu IMC é de {imc:.2f}, Levemente acima do peso')

if imc >= 18.1 and imc < 24.9:
  print(f'Seu IMC é de {imc:.2f}, Peso ideal (parabéns)')

if imc <= 18:
  print(f'Seu IMC é de {imc:.2f}, Abaixo do peso')


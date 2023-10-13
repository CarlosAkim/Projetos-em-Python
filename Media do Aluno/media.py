nota = []

for n in range(1,5):
  try:
    nota.append(float(input(f"Digite o valor da nota da prova {n}°: ")))
  except ValueError:
    print('Valor digitado não é um numero, tente novamente.')
  else:
    continue
  n+=n

provas = len(nota)
media = 0
soma = 0
for n in nota:
  soma += n
  media = soma / provas

if media > 70:
  #aprovado
  print('Aluno aprovado')
elif media >= 40 and media <=70:
  #teste
  print('Aluno tera que fazer um novo exame, para passar')
  while True:
    try:
      novaNota = float(input('Digite o valor da nota obtida do novo exame: '))
    except ValueError:
      print('Ops: Valor digitado não é um numero, tente novamente')
      continue
    else:
      resultado = (media + novaNota) / 2
      if resultado >= 50:
        print('Aluno aprovado, Parabens')
        break
      else:
        print('Aluno reprovado')
        break


else:
  #reprovado
  print('Aluno Reprovado')
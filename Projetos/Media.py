  # Lista para armazenar as notas
  nota = []

  # Loop para solicitar as notas das provas
  for n in range(1, 5):
      try:
          # Solicita ao usuário a nota da prova n e converte para float
          nota.append(float(input(f"Digite o valor da nota da prova {n}°: ")))
      except ValueError:
          # Trata o erro caso o valor digitado não seja um número válido
          print('Valor digitado não é um número, tente novamente.')
      else:
          continue  # Continua para a próxima iteração do loop
      

  # Calcula o número de provas
  provas = len(nota)
  # Inicializa a média e a soma das notas
  media = 0
  soma = 0

  # Loop para calcular a soma das notas
  for n in nota:
      soma += n
      # Calcula a média das notas
      media = soma / provas

  # Verifica se a média é maior que 70
  if media > 70:
      # Aluno aprovado
      print('Aluno aprovado')
  # Verifica se a média está entre 40 e 70
  elif media >= 40 and media <= 70:
      # Aluno deve fazer um novo exame
      print('Aluno terá que fazer um novo exame, para passar')
      while True:
          try:
              # Solicita ao usuário a nota do novo exame
              novaNota = float(input('Digite o valor da nota obtida no novo exame: '))
          except ValueError:
              # Trata o erro caso o valor digitado não seja um número válido
              print('Ops: Valor digitado não é um número, tente novamente')
              continue  # Continua solicitando até que um valor válido seja fornecido
          else:
              # Calcula a nova média considerando a nota do exame
              resultado = (media + novaNota) / 2
              if resultado >= 50:
                  # Aluno aprovado após o novo exame
                  print('Aluno aprovado, Parabéns')
                  break  # Sai do loop
              else:
                  # Aluno reprovado após o novo exame
                  print('Aluno reprovado')
                  break  # Sai do loop

  # Se a média for menor que 40
  else:
      # Aluno reprovado
      print('Aluno Reprovado')

numero = [int(input('Digite um valor: '))]
print('Quantas vezes gostaria de repetir ? :')
x = int(input(':'))
k =1
while k < x:
    numero += [int(input('Digite um valor: '))]
    k+=1


z = []
contagem = 0
for j in numero:
    if z == []:
       z.append(j)
    elif j > z[0]:     
        if j > z[contagem-1]:
                z.insert(contagem,j)
        else:
            contador = contagem
            while True:
                contador = contador - 1
                if j > z[contador-1]:
                    z.insert(contador,j)
                    break                       
    else:
        z.insert(0,j)
    contagem+=1
print(z)

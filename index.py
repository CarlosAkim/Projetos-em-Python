numero = [1,6,2,4,8,2,0,4,2,9,5,7,9,8,7,22,14,65,2,1,5]

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


lista = []
soma = 0

while True:
    listaNum = input('Digite números inteiros e receba a soma deles como resultado e deixe em branco para parar: ')

    if listaNum == '':
        print('O programa será encerrado...')
        break
    else:
        listaNum = int(listaNum)
        lista.append(listaNum)
        soma += listaNum

print('Os números inseridos foram ', lista)
print('A soma dos números é ', soma)
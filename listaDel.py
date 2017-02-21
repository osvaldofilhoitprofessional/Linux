
lista = []
soma = 0

while True:

    listaObj = str(input('Digite nomes para popular a lista e deixe em branco para parar: '))
    if listaObj == '':
        break
    else:
        lista.append(listaObj)

remover = str(input('Digite um nome para ser removido: '))

for obj in range(len(lista)-1):

    if lista[obj] == remover:
        soma += 1
        lista.remove(remover)

print('Foi(ram) removido(s) ', soma, 'ocorrência(s) de ', remover)

print('A lista atual é ', lista)
ano = int(input('Informe um ano: '))
if ano % 4 == 0:
        print('O ano é bissexto.')
else:
        print('O ano não é bissexto.')
        while ano % 4 != 0:
                ano = ano + 1
                print('O próximo ano bissexto vai ser:', ano)
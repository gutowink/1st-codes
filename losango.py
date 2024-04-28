losango = int(input('Digite o valor do losango: '))
tamanho = losango // 2
if losango % 2 == 0:
    losango += 1
    print('Número par, adicionando + 1 para ficar ímpar:', losango)

for altura in range(tamanho + 1):
    print(' ' * (tamanho - altura) + '*' * (2 * altura + 1))
    
for altura in range(tamanho):
    losango -= 2
    print(' ' * (altura + 1) + '*' * losango)
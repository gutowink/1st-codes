num = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
for i in range(num):
    fatorial *= (i + 1)
print(f'O fatorial de {num} é: {fatorial}')

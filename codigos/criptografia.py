pergunta = input('Você deseja criptografar ou descriptografar uma frase? [1/2]: ')
if pergunta == '1':
    frase = input('Digite a frase que você deseja criptografar: ')
    frase_formatada = frase.capitalize()
    desmontar = [letra for letra in frase_formatada]
    lista = []
    frase_remontada = []
    for i in range(len(frase_formatada)):
        lista.append(ord(desmontar[i]))

    for i in range(len(lista)):
        lista[i] += 2

    for i in range(len(frase_formatada)):
        frase_remontada += (chr(lista[i]))
    criptografia = ','.join(frase_remontada)
    criptografia02 = criptografia.replace(',', '')
    print(f'A frase que você digitou criptografada é: {criptografia02}')
else:
    if pergunta == '2':
        frase = input('Digite a frase que você deseja criptografar: ')
        frase_formatada = frase.capitalize()
        desmontar = [letra for letra in frase_formatada]
        lista = []
        frase_remontada = []
        for i in range(len(frase_formatada)):
            lista.append(ord(desmontar[i]))

        for i in range(len(lista)):
            lista[i] -= 2

        for i in range(len(frase_formatada)):
            frase_remontada += (chr(lista[i]))
        criptografia = ','.join(frase_remontada)
        criptografia02 = criptografia.replace(',', '')
        print(f'A frase que você digitou descriptografada é: {criptografia02}')
    else:
        print('Fora das opções.')
        exit()
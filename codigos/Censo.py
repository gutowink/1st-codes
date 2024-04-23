idade = int(input('Informe sua idade: '))
idade = 2024 - idade
if idade > 150 or idade < 0:
    print('Idade inválida, reprovado!')
else:
    estudante = input('Informe se você é estudante com [S/N]: ')
    if estudante != 'S' and estudante != 's' and estudante != 'N' and estudante != 'n':
        print('Resposta inválida, reprovado!')
    else:
        if idade < 14 and estudante == 'n' or estudante == 'N':
            print('Aprovado com ressalas.')
        else:
            trabalho = input('Informe se você trabalha com [S/N]: ')
            if trabalho != 'S' and trabalho != 's' and trabalho != 'n' and trabalho != 'N':
                print('Resposta inválida, reprovado!')
            else:
                if idade < 14 and trabalho == 's' or trabalho == 'S':
                    print('Cadastro inválido, reprovado!')
                elif idade > 14 and idade < 16:
                    if trabalho == 's' or trabalho == 'S':
                        print('Aprovado com ressalas.')
                else:
                    if trabalho == 'S' or trabalho == 's':
                        regime = input(
                            'Qual regime do seu trabalho? "mei", "estag" ou "outro" Escolha uma dentre as opções '
                            'disponiveis: ')
                        if regime == 'mei' or regime == 'estag' or regime == 'outro':
                            renda = int(input('Informe a sua renda mensal: '))
                            if renda < 0:
                                print('Renda inválida, reprovado!')
                            else:
                                if regime == 'mei' and renda > 6750:
                                    print('Cadastro inválido, reprovado!')
                                elif regime == 'estag' and estudante == 'n' or estudante == 'N':
                                    print('Cadastro inválido, reprovado!')
                                else:
                                    print('Aprovado.')
                    else:
                        aposentado = input('Informe se você é aposentado com [S/N]: ')
                        if aposentado == 'S' or aposentado == 's':
                            if idade < 62:
                                print('Aprovado com ressalas.')
                            else:
                                print('Aprovado.')
                        else:
                            print('Aprovado.')
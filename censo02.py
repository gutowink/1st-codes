entrevistas = [
    # nome, ano_nasc, estuda, trabalha, renda
    ['Albano Marcelo', 2000, 's', 'mei', 2000],
    ['Felipe Matheus', 1893, 'n', 'aposentado', 5500],
    ['Aécio Alfredo', 1977, 'n', 'mei', 0],
    ['Ian Danilo', 1990, 's', 'outro', 4000],
    ['Kevin Tomáz', 1972, 'n', 'outro', -1000],
    ['Karl Raul', 1890, 'n', 'mei', 8500],
    ['Celina Isaiane', 1981, 's', 'mei', -1500],
    ['Guilherme Isac', 1857, 'n', 'outro', -1000],
    ['Cristiano FerminianoAnderson Sérgio', 1898, 's', 'mei', 6000],
    ['Nicole Vanda', 2007, 's', 'n', 0],
    ['Michele Burgos', 1872, 'n', 'aposentado', 9500],
    ['Violeta Fátima', 1980, 's', 'estag', 4000],
    ['Ângela Wendy', 1864, 'n', 'outro', 4500],
    ['Albano Marés', 1937, 'n', 'outro', 5500],
    ['Ediane Mara', 1933, 'n', 'n', 8000],
    ['Luara Michele', 1902, 's', 'n', -1000],
    ['Isabela Isaiane', 2006, 's', 'mei', 6500],
    ['Isabella Lara', 1936, 's', 'estag', 9000],
    ['Fátima Graziele', 1949, 's', 'aposentado', 2000],
    ['Nádia Balestero', 2002, 'n', 'mei', -2000],
    ['Hilda Kelly', 1926, 's', 'mei', 5500],
    ['Micaela Bittencourt', 2018, 'n', 'aposentado', 2500],
    ['Beatriz Luciana', 1951, 'n', 'estag', 3000],
    ['Natal Miguel', 2022, 'n', 'outro', 9500],
    ['Christian Gil', 2001, 's', 'outro', 10000],
    ['Elói Camacho', 2019, 'n', 'aposentado', 3000],
    ['Demilson Faro', 1904, 's', 'aposentado', 5000],
    ['Juliana Delgado', 2003, 'n', 'outro', -1000],
    ['Fábio Jaziel', 2009, 'n', 'aposentado', 4500],
    ['Beto Edivaldo', 1920, 's', 'estag', 2000],
    ['Itamara Carmona', 1974, 's', 'outro', 500],
    ['Solange Zara', 1875, 's', 'aposentado', 3500],
    ['Bruno Barros', 2005, 's', 'outro', 5000],
    ['Jardel Nivaldo', 1989, 'n', 'n', -1500],
    ['Hortência Batista', 2012, 's', 'mei', 2500],
    ['Cristina Simone', 1986, 'n', 'aposentado', -2000],
    ['Mirela Rosilda', 1933, 's', 'aposentado', 4500],
    ['Suzana Eloá', 1950, 'n', 'outro', 7500],
    ['Nicole Gomes', 1990, 's', 'aposentado', 1000]
]

ANO_ATUAL = 2024
MAIS_VELHA = 0
NOME_VEIO = None
SAL_ESTAG = 0
ESTAG_NOME = None
C = 0  # número de pessoas na lista
REPROVADOS = 0
APROVADOS_COM_R = 0
APROVADOS = 0

for entrevista in entrevistas:
    nome = entrevista[0]
    ano_nasc = entrevista[1]
    idade = ANO_ATUAL - ano_nasc
    estuda = entrevista[2]
    trabalha = entrevista[3]
    renda = entrevista[4]
    C += 1
    if (trabalha == 'mei' and renda > 6750
        or trabalha == 'estag' and estuda != 's'
        or idade < 14 and trabalha != 'n'
        ):
        REPROVADOS += 1
    elif(trabalha == 'aposentado' and idade < 62
         or estuda != 's' and idade < 14
         or trabalha != 'n' and 16 > idade > 14
        ):
        APROVADOS_COM_R += 1
    else:
        APROVADOS += 1

    if (trabalha == 'mei' or trabalha == 'estag'
            or trabalha == 'outro' and renda > 0):
        if idade > MAIS_VELHA:
            MAIS_VELHA = idade
            NOME_VEIO = nome
    if trabalha == 'estag' and renda > SAL_ESTAG:
        SAL_ESTAG = renda
        ESTAG_NOME = nome
print('O estágiario com maior salário é', ESTAG_NOME, 'que recebe', SAL_ESTAG)
print('A pessoa mais velha trabalhando é', NOME_VEIO, 'com', MAIS_VELHA, 'anos.')
print('Total de pessoas entrevistadas:', C,
      'Dentre eles:', REPROVADOS, 'Reprovados,',
      APROVADOS_COM_R, 'Aprovados com ressalvas e',
      APROVADOS, 'Aprovados.')

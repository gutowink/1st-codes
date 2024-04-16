t = 3
c = 1
print('você tem 3 tentativas para acertar a senha, senão o algoritmo irá encerrar.')
senhac = 1234
senha = float(input('Qual é a senha?'))
t = t - 1
if senha != senhac:
    while t > 0 and senha != senhac:
        print('Senha incorreta, mais {} tentativas'.format(t))
        senha = float(input('Qual é a senha?'))
        c = c + 1
        t = t - 1
else:
    print('senha correta')
if senha == senhac:
    if c >= 2:
        print('senha correta')
    print('Acesso permitido!')
else:
    print('Acesso negado!')
print('A senha foi digitada {} vezes'.format(c))
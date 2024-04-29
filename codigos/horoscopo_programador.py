signos = ('Python','Fortran','Rust','Go','Java','JavaScript','C','PHP','Haskell','Perl','Swift','Kotlin')
mes = int(input('Digite o mês do seu nascimento em número inteiro, de 1 para janeiro até 12 para dezembro: '))
if mes <= 0 or mes >= 13:
        print('Você não é um programador.')
else:
        print('Seu signo de programador é:', signos[mes - 1])
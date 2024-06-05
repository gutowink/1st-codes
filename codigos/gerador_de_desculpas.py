import random

def introducao():
    num_introducao = random.randint(1, 3)
    if num_introducao == 1:
        return 'Você não vai acreditar, mas'
    elif num_introducao == 2:
        return'Nem imagina o que vou te contar'
    else:
        return 'Parece mentira mas'

def objetivo():
    num_objetivo = random.randint(1, 3)
    if num_objetivo == 1:
        return 'meu pokémon favorito'
    elif num_objetivo == 2:
        return 'o cachorro do vizinho'
    else:
        return 'o Et Bilú'
def evento():
    num_evento = random.randint(1, 3)
    if num_evento == 1:
        return 'roubou minha bicicleta.'
    elif num_evento == 2:
        return 'hackeou meu instagram.'
    else:
        return 'não sabe tocar piano.'

tarefa = input('tarefa que precisa de uma desculpa: ')
print(f'{introducao()} {tarefa} porque {objetivo()} {evento()}')
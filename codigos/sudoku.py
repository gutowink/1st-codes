sudoku_grid_B = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 8, 6, 7, 5, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 5, 2, 3, 4, 1, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]
sudoku_grid_A = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

NUM = 0
soma = 0
SOMA = 0
aux = 0

for linha in sudoku_grid_B:
    for coluna in linha:
        NUM += coluna
if NUM == 405:  # 405 = 9 linhas com total de 45. 45 = 1+2+3+4+5+6+7+8+9
    print('Linhas válidas.')
else:
    print('Linhas inválidas.')
    exit()
print('Checando as colunas...')

for j in range(len(sudoku_grid_B)):
    for i in sudoku_grid_B:
        SOMA += i[j]
    aux += SOMA
    SOMA = 0
    if aux > 45 or aux < 45: # Se a aux que calcula a soma da coluna é diferente de 45 então esta coluna está errada.
        soma += 1 # Esta variável recebe + 1 toda vez que alguma coluna inválida for identificada.
        aux = 0 # A aux é zerada para começar do zero a contagem da próxima coluna.
    else:
        aux = 0 # Caso a coluna esteja correta também vai ser zerada para calcular a próxima coluna.
if soma != 0:
    print('Colunas inválidas.')
    exit()
else:
    print('Colunas válidas.')

print('Checando os quadrantes...')
def check_row(list_full):
    for ligne in list_full:
        if len(ligne) != len(set(ligne)):
            return False
    return True

def check_column(list_full):
    for colonne in range(9):
        col = [list_full[row][colonne] for row in range(9)]
        if len(col) != len(set(col)):
            return False
    return True

def check_carre(list_full):
    for ligne in range(0, 9, 3):
        for colonne in range(0, 9, 3):
            carre = []
            for i in range(3):
                for j in range(3):
                    carre.append(list_full[ligne+i][colonne+j])
            if len(carre) != len(set(carre)):
                return False
    return True

def check_sudoku(list_full):
    return check_column(list_full) and check_carre(list_full) and check_row(list_full)

def afficher(data):
    for i in range(9):
        for j in range(9):
            print(data[i][j], end=" ")
        print()

def find_zero(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == 0:
                return i, j
    return -1, -1

def valid_move(data, row, col, num):
    # Vérifie la ligne
    for i in range(9):
        if data[row][i] == num:
            return False

    # Vérifie la colonne
    for i in range(9):
        if data[i][col] == num:
            return False

    # Vérifie le carré
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if data[i + startRow][j + startCol] == num:
                return False

    return True

def solve_sudoku(data):
    row, col = find_zero(data)
    if row == -1:  # Si aucune case vide n'est trouvée, la grille est résolue
        return True
    for num in range(1, 10):
        if valid_move(data, row, col, num):
            data[row][col] = num
            if solve_sudoku(data):
                return True
            data[row][col] = 0  # Efface le mouvement s'il ne mène pas à une solution
    return False

grille = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

print("Grille de Sudoku avant résolution:")
afficher(grille)

if solve_sudoku(grille):
    print("\nSudoku résolu:")
    afficher(grille)
else:
    print("Pas résolvable.")

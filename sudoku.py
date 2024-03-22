from dokusan import generators

def convertir_grille_dokusan(grille_str):
    grille = []
    lignes = [grille_str[i:i+9] for i in range(0, len(grille_str), 9)]
    for ligne in lignes:
        grille.append([int(char) if char != '.' else 0 for char in ligne])  # Remplace '.' par 0 et convertit en int
    return grille

# Check la ligne
def check_row(list_full):
    doublon_row = False

    for ligne in list_full:
        box = set()
        for item in ligne:
            if item in box: # Si un même chiffre revient, alors doublon_row deviendra true
                doublon_row = True
            else:
                box.add(item) # Ajoute chaque chiffre dans box, qui ne contiendra que des chiffres uniques (grâce au set())

    if doublon_row  :
        return False
    else:
        return True

#Check la colonne
def check_column(list_full):
    doublon_column = False

    for colonne in range(9):
        box_columns = set()
        for item in list_full:
            if item[colonne] in box_columns:
                doublon_column = True
            else:
                box_columns.add(item[colonne])

    if doublon_column:
        return False
    else:
        return True

#Check le carré
def check_carre(list_full):
    list_carre = []

    for ligne_full in range(0, 9, 3):
        for colonne_full in range(0, 9, 3):
            carre = []
            for row in range(ligne_full, ligne_full + 3):
                for col in range(colonne_full, colonne_full + 3):
                    carre.append(list_full[row][col])
            list_carre.append(carre)
            if len(carre) != len(set(carre)):
                return False
    return True

#Vérifie si la grille du sudoku est valide
def check_sudoku(list_full):
    return check_column(list_full) and check_carre(list_full) and check_row(list_full)

#Affiche la grille du sudoku
def afficher(data):
    for i in range(9):
        for j in range(9):
            print(data[i][j], end=" ")
        print()

#Trouve le zero sur la grille
def find_zero(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == 0:
                return i, j
    return None, None

#Check les numéros sur les lignes, colonnes et carrés pour savoir quelle chiffre il peut mettre
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
    if row == None:
        return True
    for num in range(1, 10):
        if valid_move(data, row, col, num):
            data[row][col] = num
            if solve_sudoku(data):
                return True
            data[row][col] = 0
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

grille_str = str(generators.random_sudoku(avg_rank=150))
grille = convertir_grille_dokusan(grille_str)

print("Grille de Sudoku avant résolution:")
afficher(grille)

if solve_sudoku(grille):
    print("\nSudoku résolu:")
    afficher(grille)
else:
    print("Pas résolvable.")

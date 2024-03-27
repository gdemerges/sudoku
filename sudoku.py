from dokusan import generators

# Permet de convertir de string en int
def convertir_grille_dokusan(grille_str):
    grille = []
    lignes = [grille_str[i:i+9] for i in range(0, len(grille_str), 9)]
    for ligne in lignes:
        grille.append([int(char) if char != '.' else 0 for char in ligne])
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
    # On isole chaque carré 3x3
    for ligne_full in range(0, 9, 3):
        for colonne_full in range(0, 9, 3):
            carre = []
            # On parcours les 3 lignes et colonnes de chaque carré
            for row in range(ligne_full, ligne_full + 3):
                for col in range(colonne_full, colonne_full + 3):
                    carre.append(list_full[row][col])
            list_carre.append(carre)
            # On vérifie que le carré est bien unique
            if len(carre) != len(set(carre)):
                return False
    return True

#Vérifie si la grille du sudoku est valide avec les 3 fonctions créées précédemment
def check_sudoku(list_full):
    return check_column(list_full) and check_carre(list_full) and check_row(list_full)

#Affiche la grille du sudoku
def afficher(data):
    for i in range(9):
        for j in range(9):
            print(data[i][j], end=" ")
        print()

#Trouve le zero en parcourant la grille
def find_zero(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == 0:
                return i, j
    return None, None # Si il n'y a plus de 0, renvoie None

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

    # Vérifie le carré en soustrayant le reste de la division par 3
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if data[i + startRow][j + startCol] == num:
                return False
    return True

# Permet de résoudre le sudoku en trouvant le zero, puis en checkant où il peut mettre le numero
def solve_sudoku(data):
    row, col = find_zero(data)
    if row == None: # Si None alors la grille est résolu
        return True
    for num in range(1, 10):
        if valid_move(data, row, col, num):
            data[row][col] = num
            if solve_sudoku(data):
                return True
            data[row][col] = 0 # Si pas de solution valide, alors remet 0 et essaye le numero suivant avec la récursivité
    return False

def choice_difficulty():
    print("Choisissez la difficulté de votre grille de Sudoku:")
    print("1. Facile")
    print("2. Moyenne")
    print("3. Difficile")

    choix = input("Entrez le numéro correspondant à votre choix (1, 2 ou 3): ")

    # Renvoie différentes grilles avec un niveau différent suivant le choix saisis
    if choix == '1':
        grille_difficulty = generators.random_sudoku(avg_rank=50)
    elif choix == '2':
        grille_difficulty = generators.random_sudoku(avg_rank=150)
    elif choix == '3':
        grille_difficulty = generators.random_sudoku(avg_rank=350)
    else:
        print("Saisie incorrecte. Veuillez réessayer.")
        return choice_difficulty()
    grille = convertir_grille_dokusan(str(grille_difficulty))
    return grille

def main():
    if check_sudoku(grille):
        print("La grille de Sudoku est valide.")
    else:
        print("La grille de Sudoku n'est pas valide.")

    grille = choice_difficulty()

    print("Sudoku avant résolution:")
    afficher(grille)

    if solve_sudoku(grille):
        print("\nSudoku résolu:")
        afficher(grille)
    else:
        print("Pas résolvable.")

def check_row(list_full):
    doublon_row = False

    for ligne in list_full:
        box = set()
        for item in ligne:
            if item in box:
                doublon_row = True
            else:
                box.add(item)

    if doublon_row  :
        return False
    else:
        return True

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

def check_sudoku():
    if check_column(list_full) and check_carre(list_full) and check_row(list_full) == True:
        print("Soduku valide")
    else:
        print("Soduku non valide")

list_full = [
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

check_sudoku()


grille = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def afficher(data):
    for i in range(9):
        for j in range(9):
            print(data[i][j], end = " ")
        print()

afficher(grille)

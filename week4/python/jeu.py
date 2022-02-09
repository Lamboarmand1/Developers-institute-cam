import  sys

# interface de jeu 3*3
board = [[" "," "," "] , [" "," "," "] , [" "," "," "]]

def game():

    # On fait tourner le jeu tant qu'il y'a pas de victoire.

    while True :
        turn(board)

    # On fait jouer le joueur x et le joueur 0.

def turn(board):
    play("x", board)
    play("0", board)

# les joueurs ont les memes tours de jeu.
    
def play(player, board):
    #On affiche l'interface de jeu.
    print_board(board)
    #Si la partie est deja terminer alors on arret le jeu.
    check_for_tie(board)
    #Si le jeu n'est pas terminer alors on demande au joueur de choisir une ligne et une colonne.
    print("C'est au tour du joueur"+player+ +".")
    print("ligne? (0,1 ou 2)")
    lines = int(input())
    print("colonne? (0,1 ou 2)")
    columns = int(input())
    #Vue le joueur ne peut que jouer dans une case vide alors on verifie si il a fait le bon choix.
    if  board[lines][columns] == "":
        #Si le joueur a jouer sur une case vide alors on le print.
        board[lines][columns]= player
        #Si il a aligner trois case identique alors on 
        check_win(player, board)
    else:
        #Si le joueur a joue sur une case non vide.
        invalid_choice() 

#creer le tableau

def print_board(board):
    #On affiche la premiere ligne de notre tableau.
    print("-------")
    #On desinne toutes les lignes du tableau de 0-2. 
    for x in range(0, 3):
        # les colonnes du tableau de 0-2.
        for y in range(0, 3):
            #On affiche le contenu du tableau avec la separation|
            print("|" +board[x][y], end="")

            #On met la barre pour signifie la fin de la ligne|
            print("|")
            #On met la ligne de separation
            print("--------")

#On check si le joueur a gagner.
def check_win(player, board):
    #On verifie si les lignes , les diagonales et les colonnes sont alignes.
    check_alignments (player, board(lines) + board(columns) + board(diagonals))
#Etant donner qu'un alignement est un symbole du joueur.
def check_alignments_for(player, lines):
    if lines == player * 3:
        game_is_over(player)    
#On teste tout les alignements possibles du tableau
def check_alignments (player, joueur):
    for x in range(0, len(joueur)):
        check_alignments_for(player, joueur[x])
#creons une fonction qui va renvoyer les colonnes.
def columns(board):
    Cboard = [[]]*3
    for x in range(0, 3):
        Cboard = [" "] * 3
    for x in range(0, 3):
        for y in range(0, 3):
            Cboard[x][y] = board[x][y]
    return Cboard
#Creons une fonction qui va renvoyer les lignes
def lines(board):
    return board
#Creons une fonction qui va renvoyer les diagonales
def diagonals(board):
    return [[board[0][0],board[1][1],board[2][2]],[board[2][0],board[1][1],board[0][2]]]
#On creer une fonction qui va compter les cases vides au fur et a mesure qu'on avances.
def count_empty_cells(board):
    a = 0 
    #On parcour toutes les lignes
    for x in range(0, 3):
        #on parcour egalement toutes les colonnes
        for y in range(0, 3):
            if board[x][y] == " ":
                a = a+1
    return a
#On teste si il reste encore des cases vides
def check_for_tie (board):
    if count_empty_cells == 0 :
        #si il ne reste plus de case vide alors la partie est finie sur une egalité
        print("La partie est fini sur une egalité du joueur1 et joueur2")
        sys.exit(0)
#On arret le jeu sur a une invalidité des joueurs
def invalid_choice():
    print("invalide")
    sys.exit(0)
#On determine le gagnant et on stopper le jeu
def game_is_over(player, tableau):
    print(player + "a gagné")
    print_board(board)
    sys.exit(0)

game()
print_board(board)                                


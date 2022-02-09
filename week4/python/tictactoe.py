#On initialise le tableau de nos cases variables
tableau=[[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
#ou tableau=[0,1,2,3,4,5,6,7,8]

#On initialise nos joueurs
player1 = 'X'
player2 = 'O'

#La fonction a appeler pour afficher le tableau 
def display_board():
    grid='''*****************
*  {} |  {} |  {}  *
* ___|____|____ *
*  {} |  {} |  {}  *
* ___|____|____ *
*  {} |  {} |  {}  *
*****************
    '''.format(tableau[0][0],tableau[0][1],tableau[0][2],
    tableau[1][0],tableau[1][1],tableau[1][2],
    tableau[2][0],tableau[2][1],tableau[2][2])
    #"""""""".format(tableau[0],tableau[1],tableau[2],tableau[3],tableau[4],tableau[5],
    #tableau[6],tableau[7],tableau[8])

    print(grid)

#La fonction pour prendre les input des joueurs
def player_input(player):
    ligne =int(input(f'Cher {player} Vous voulez jouer sur quelle ligne ? : '))
    colonne =int(input(f'Cher {player} Vous voulez jouer sur quelle colonne ? : '))
    tableau[ligne-1][colonne-1] = player
    return check_win()
    

#La fonction pour verifier si il y a victoire et qui a gagné
def check_win():
    if tableau[0][0]==tableau[0][1]==tableau[0][2]==player1 :
        print(f' Congratulations {player1} vous avez gagné ')
        return True

#La fonction play pour coordonner tout le programme
def play():
    print('WELCOME TO TIC TAC TOE\n')
    print('TIC TAC TOE\n')
    display_board()
    for tour in range(9):
        if tour%2 == 0 :
            print(f'C est le tour de {player1}') 
            win = player_input(player1)
            display_board()
            if win :
                print('End of game')
                break
        else:
            print(f'C est le tour de {player2}') 
            player_input(player2)
            display_board()
    if tableau[0][0]!= ' ' and tableau[0][1]!= ' ' and tableau[0][2]!= ' ' and
    tableau[1][0]!= ' ' and tableau[1][1]!= ' ' and tableau[1][2]!= ' ' and
    tableau[2][0]!= ' ' and tableau[2][1]!= ' ' and tableau[2][2] != ' ':
        print('No one won goodbye')


play()
import random
#liste des mots
mots = ['telephone','developpeur','dictionnaire','avion','internet','partenaire','serveur','patron']
#l'ordinateur choisir un au hasard
computer = random.choice(mots)
print(computer)

display = '_'*len(computer)

error = 5
print('Vous avez %d :' %error +'tentative(s)')

for x in computer:
    armand = display.split(' ')

print('_'.join(armand))

while error > 0:

    user = input('Entrer votre lettre : ')
    if user in computer:
        print('Bravo mon amie')
        
        for count in enumerate(computer):
            if user == 1:
                armand[count] = user
              
         

    else:
     
       error = error - 1
       print('Tentatives restantes : %d' %error)

    print(' '.join(armand))
      
    if '_' not in armand:
        print('mon amie tu as gagné des %d erreur(s)' % error) 
        break  

if '_' in armand:
    print('lost mon amie')
    print('le mot etait %s : ' %computer) 

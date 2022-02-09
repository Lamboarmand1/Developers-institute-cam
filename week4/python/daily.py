
from Point import Point
import math

class Cercle:
    #initialisation du cercle (on affecte 0 partout)
    def __init__(self, centre=Point(0,0),rayon=0, diametre=0):
        self.centre = centre
        self.rayon = rayon
        self.diametre = diametre
    # la fonction qui retourne les valeurs du cercles de facon specifique
    def val_centre(self):
        return self.centre
    def val_rayon(self):
        return self.rayon
    def val_diametre(self):
        return self.diametre
    # la fonction pour calculer l'aire du cercle
    def calculer_Aire(self):
        return math.pi * (self.rayon ** 2) 
    #imprimez les valeurs du cercle     
    def __str__(self):
        return "centre = " + str(self.centre) + ", rayon = " + str(self.rayon) + ", diametre = " + str(self.diametre) 
    # fonction pour comparer les cercles
    def __gt__(self, c1):

        grandeur = False
        if self.centre > c1.centre and self.rayon > c1.rayon:
            grandeur = True
        return grandeur

    def __eq__(self, c1):
        egal = False
        if self.centre == c1.centre and self.rayon == c1.rayon and self.diametre == c1.diametre:
            egal = True    
        return egal
    #testons


    def main():
        c1 = Cercle()
        c2 = Cercle(Point(4,8), 12, 6)
        c3 = Cercle(Point(3,6), 10, 5)
        if c2 == c3 : 
            print(str(c2))
        print(c2.calculer_surface())
        if c2 > c3 :
            print(str(c2))
        print("voici le cercle le plus grand :" +c2.calculer_surface() )    
    if __name__ == "__main__":
        main()               
        
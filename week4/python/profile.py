from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo
from liste import listeInscrit
import service as serv

class Personnage():
    def __init__(self,Nom, Capital, Sous_Region, Population, Drapeau):
        self.Nom = Nom
        self.Capital = Capital
        self.Sous_Region = Sous_Region
        self.Population = Population
        self.Drapeau = Drapeau

    def __eq__(self,other):
        return(self.Nom == other.Nom and self.Capital == other.Capital and self.Sous_Region == other.Sous_Region and self.Population == other.Population)

def Parcourir():
    global imageName
    Imn = askopenfilename(initialdir="/",title="selectionner une image",filetypes=(("png files","*.png"),("jpeg files","*.jpg")))
    if Imn:
        imageName=Imn
    if imageName:
        text = imageName.split("/")
        DrapeauEntre.configure(text=".../"+text[-1])

def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
        return 0
def Valider():
    global imageName
    print(888)
    Drapeau = imageName
    if NomEntre.get() and CapitalEntre.get() and Sous_RegionEntre.get() and PopulationEntre.get() and Drapeau:
        print(4566)
        pn = Personnage(NomEntre.get(),CapitalEntre.get(),Sous_RegionEntre.get(),PopulationEntre.get(),Drapeau)
        print(pn.Drapeau)
        serv.ajouter(pn)
         
       
        showinfo(title="Validation reussie",message="{} a bien ete ajouter".format(NomEntre.get()))
    else:
        showerror(title="Formulaire Invalide",message="Toutes les champs doivent etre remplir")


def Reinitialiser():
    global imageName
    NomEntre.delete(0,END)
    CapitalEntre.delete(0,END)
    Sous_RegionEntre.delete(0,END)
    PopulationEntre.delete(0,END)
    imageName=''
    DrapeauEntre.configure("Aucune image selectionner")

imageName= ''    


fen = Tk()
fen.geometry("400x350")
fen.title("page d'inscription")

contenu = Canvas(fen,bg="skyblue")

fontLabel = 'arial 13 bold'
fontEntre = 'arial 13 bold'

Nom = Label(contenu, text="Votre Pays :",font = fontLabel, fg='black',bg="skyblue")
Capital = Label(contenu, text="Votre Capital :",font = fontLabel, fg='black',bg="skyblue")
Drapeau = Label(contenu, text="Votre Drapeau :",font = fontLabel, fg='black',bg="skyblue")
Sous_Region = Label(contenu, text="Votre Sous Region :",font = fontLabel, fg='black',bg="skyblue")
Population = Label(contenu, text="Votre Population :",font = fontLabel, fg='black',bg="skyblue")
Validation = Label(contenu, text="Entrer Les Information De Votre Pays Ici :",font = fontLabel, fg='black',bg="skyblue")


NomEntre = Entry(contenu, font=fontEntre)
CapitalEntre = Entry(contenu, font=fontEntre)
Sous_RegionEntre = Entry(contenu, font=fontEntre)
PopulationEntre = Entry(contenu, font=fontEntre)
DrapeauEntre = Label(contenu, text="Aucune Image Selectionner", font = 'arial 8 bold', fg='skyblue',bg='black')
ButtonParcourir = Button(contenu, text = "pr",command=Parcourir, fg='skyblue',bg='black')


Validation.grid(row=0,column=0,columnspan=3)
Nom.grid(row=1,column=0,sticky=E,padx=5,pady=5)
Capital.grid(row=2,column=0,sticky=E,padx=5,pady=5)
Sous_Region.grid(row=3,column=0,sticky=E,padx=5,pady=5)
Population.grid(row=4,column=0,sticky=E,padx=5,pady=5)
Drapeau.grid(row=5,column=0,sticky=E,padx=5,pady=5)

NomEntre.grid(row=1,column=1,padx=5,pady=5)
CapitalEntre.grid(row=2,column=1,padx=5,pady=5)
Sous_RegionEntre.grid(row=3,column=1,padx=5,pady=5)
PopulationEntre.grid(row=4,column=1,padx=5,pady=5)
DrapeauEntre.grid(row=5,column=1,padx=5,pady=5,sticky=W)
ButtonParcourir.grid(row=5,column=1,padx=5,pady=5,sticky=E)

b1 = Button(fen,text="Valider",command=Valider,width=10, fg='skyblue',bg='black')
b2 = Button(fen,text="Reinitialiser",command=Reinitialiser,width=10, fg='skyblue',bg='black')
b3 = Button(fen,text="Voir La Liste",command=lambda:listeInscrit(fen),width=10, fg='skyblue',bg='black')


b1.grid(row=4,column=0,pady=5)
b2.grid(row=5,column=0,pady=5)
b3.grid(row=6,column=0,pady=5)

contenu.grid(row=0,column=0,padx=5,pady=5)

fen.mainloop()

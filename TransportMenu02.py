from tkinter import *
from tkinter import messagebox
from file import File
from Transport import *

#creation list vide
lista = []

fenetre1 = Tk()

fenetre1.geometry("900x600")
fenetre1.title('Formulaire')

# creation de variables pr récupérer les valeurs du petit formulaire
societeProprietaire = StringVar()
couleur = StringVar()
age = IntVar()
longueurAiles = IntVar()
largeurAiles = IntVar()


lbl0 = Label(fenetre1, text='Nos Avions !', fg='red', width=22, font=("bold", 20)).place(x=240, y=20)

label = Label(fenetre1,text = "Liste des Avions Rouges", fg='red', width=28, font=("bold", 16)).place(x=520, y=90)


lbl1 = Label(fenetre1, text="Societé Propriétaire", width=15, font=("bold", 10)).place(x=80, y=130)
Entre1 = Entry(fenetre1, textvar=societeProprietaire, justify=LEFT, width=40).place(x=240, y=130)

lbl2 = Label(fenetre1, text="Couleur", width=15, font=("bold", 10)).place(x=45, y=170)
Entre2 = Entry(fenetre1, textvar=couleur, justify=LEFT, width=40).place(x=240, y=170)

lbl3 = Label(fenetre1, text="Age", width=15, font=("bold", 10)).place(x=37, y=210)
Entre3 = Entry(fenetre1, textvar=age, justify=RIGHT, width=40).place(x=240, y=210)

lbl4 = Label(fenetre1, text="Longueur Ailes", width=15, font=("bold", 10)).place(x=64, y=250)
Entre4 = Entry(fenetre1, textvar=longueurAiles, justify=RIGHT, width=40).place(x=240, y=250)

lbl5 = Label(fenetre1, text="Largeur Ailes", width=15, font=("bold", 10)).place(x=60, y=290)
Entre5 = Entry(fenetre1, textvar=largeurAiles, justify=RIGHT, width=40).place(x=240, y=290)


listbox = Listbox(fenetre1, width=60, height=20, selectmode=SINGLE)
listbox.place(x=510, y=120)

fileAvions = File()

def creation():
    messagebox.showinfo("Résumé Liste des Avions Rouges",
                        "SocietéPropriétaire:" + f"{societeProprietaire.get()} \nCouleur:{couleur.get()} \nAge:{age.get()} \nLongueurAiles:{longueurAiles.get()}  ")
    avion1 = Avion(societeProprietaire.get(), couleur.get(), age.get(), longueurAiles.get(), largeurAiles.get())
    avion1.calculRapport()
    print(f'{avion1.imprimir()} La Rapport est : {avion1.calculRapport()}')
    fileAvions.enfiler(f"{avion1.imprimir()} La Rapport est : {avion1.calculRapport()} \n")
    lista.append(avion1)
    #print(lista)
def listedesrouges():
    k=0
    while k<len(lista):
        condstr = lista[k].couleur
        if condstr == 'ROUGE':
            print("sociétés propriétaires ",lista[k].societéPropriétaire," longueur",lista[k].longueurAiles)
            listboxstr = lista[k].societéPropriétaire+" "+lista[k].couleur
            listbox.insert(END, listboxstr)
        k += 1
def listedesnoms():
    k=0
    while k<len(lista):
       print("sociétés propriétaires ",lista[k].societéPropriétaire," longueur",lista[k].longueurAiles)
       f1 = open("monFichier02.txt", "a")
       print(lista[k].societéPropriétaire, file=f1)
       f1.close()
       k += 1


bouton1 = Button(fenetre1, bg='brown',  width=15, fg='white', text='Création', command=creation).place(x=50, y=430)
bouton2 = Button(fenetre1, bg='brown',  width=15, fg='white', text='Liste des rouges', command=listedesrouges).place(x=180, y=430)
bouton3 = Button(fenetre1, bg='brown',  width=15, fg='white', text='Liste des noms', command=listedesnoms).place(x=310, y=430)

bouton4 = Button(fenetre1, bg='brown',  width=15, fg='white', text='Quitter', command=fenetre1.destroy).place(x=200, y=500)


fenetre1.mainloop()

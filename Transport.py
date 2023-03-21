class Locomotion:
    def __init__(self):
        self.societéPropriétaire=''
        self.couleur=''
        self.age=0
    def __init__(self, societéPropriétaire, couleur, age):
        self.societéPropriétaire=societéPropriétaire
        self.couleur=couleur
        self.age=age
    def prendreAge(self, nbAns ):
        self.age= self.age + nbAns
    def changeCouleur(self, nouvelleCouleur):
        self.couleur = nouvelleCouleur
    def imprimir(self):
      return("societéPropriétaire: {} Couleur : {} Age : {}".format(self.societéPropriétaire, self.couleur, self.age))
    def __str__(self):
          return"le moyen de locomotion est {}".format(self.societéPropriétaire)

class Avion(Locomotion):
    def __init__(self):
        self.societéPropriétaire = ''
        self.couleur=''
        self.age=0
        self.longueurAiles=0
        self.largeurAiles=0
    def __init__(self, societéPropriétaire, couleur, age, longueurAiles, largeurAiles):
        super().__init__(societéPropriétaire, couleur, age)
        self.longueurAiles=longueurAiles
        self.largeurAiles=largeurAiles
    def calculRapport(self):
       return self.longueurAiles * self.largeurAiles
    def imprimir(self):
      return super().imprimir().__str__()+" Je suis le Transport Avion Longueur Ailes : {} Largeur Ailes : {} ".format(self.longueurAiles, self.largeurAiles)

class Train(Locomotion):
    def __init__(self):
        self.societéPropriétaire = ''
        self.couleur=''
        self.age=0
        self.nombreDePassagers=0
        self.nombreDeWagons=0
    def __init__(self, societéPropriétaire, couleur, age, nombreDePassagers, nombreDeWagons):
        super().__init__(societéPropriétaire, couleur, age)
        self.nombreDePassagers=nombreDePassagers
        self.nombreDeWagons=nombreDeWagons
    def embarque(self):
       self.nombreDePassagers+=1
    def debarque(self):
       self.nombreDePassagers-=1
    def calculeLongueurTrain(self):
        return self.nombreDeWagons * 3.25
    def imprimir(self):
      super().imprimir()
      print("Je suis le Transport Tren Couleur : {} Age : {} nombre De Passagers : {} Longueur Train: calculeLongueurTrain() ".format(self.societéPropriétaire, self.couleur, self.age))


######################################
#if __name__ == '__main__':
    #avion1 = Avion('MaisonneuveTransport', 'rouge', 10, 7, 3)
    #avion1.calculRapport()
    #avion1.imprimir()
from Region import *
from Ville import *
import random
class Route:
    def __init__(self): # Constructeur
        self.villes = []
        self.poids = 0

    def ajouter_ville(self, ville): # Ajoute une ville a la route
        self.villes.append(ville) # Ajoute la ville a la liste des villes
        if len(self.villes) >= 2: # Si la route contient au moins 2 villes
            self.poids += ville.distance_vers(self.villes[-2]) # Ajoute le poids de la distance entre la ville et la ville precedente
        else:
            self.poids += 0 # Sinon, le poids est 0

    def ajouter_villes(self, villes): # Ajoute plusieurs villes a la route
        for ville in villes: # Pour chaque ville dans la liste de villes
            self.ajouter_ville(ville) # Ajoute la ville a la route

    def __str__(self): # Affiche la route
        return f"Route: {self.villes}, Poids: {self.poids}"     
    
    def mutate(self):
        # Choisissez deux indices aléatoires
        index1 = random.randint(0, len(self.villes) - 1)
        index2 = random.randint(0, len(self.villes) - 1)

        # Échangez les villes à ces indices
        self.villes[index1], self.villes[index2] = self.villes[index2], self.villes[index1]

    def fitnessReload(self,a):
        pd= self.poids
        self.poids = 0
        for i in range(len(self.villes) - 1):  # s'arrête à l'avant-dernier élément
            self.poids += self.villes[i].distance_vers(self.villes[i+1]) # ajoute la distance entre la ville i et la ville i+1
        if pd!=self.poids:
            print("Erreur de calcul de poids , modification de la valeur de poids")
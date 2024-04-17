from Ville import *
import random
class Region:
    def __len__(self):
        return len(self.villes)
    def __init__(self, number=None):
        self.villes = []
        if number is not None:
            for i in range(number):
                self.villes.append(Ville("Ville " + str(i), random.randint(0, 100), random.randint(0, 100)))
    
    def afficher_villes(self):
        for ville in self.villes:
            print(ville)

    def ajouter_ville(self, ville):
        self.villes.append(ville)
    
    def ajouter_villes(self, villes):
        for ville in villes:
            self.ajouter_ville(ville)

    def enlever_ville(self, ville):
        self.villes.remove(ville)

     def choisir_ville_aleatoire(self):
        return random.choice(self.villes)
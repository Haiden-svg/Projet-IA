from Ville import *
import random
class Region:
    def __init__(self, number=None):
        self.villes = []
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
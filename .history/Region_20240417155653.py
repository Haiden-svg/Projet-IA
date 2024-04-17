from Ville import *
import random
class Region:
    def __init__(self, villes):
        self.villes = villes

    def afficher_villes(self):
        for ville in self.villes:
            print(ville)

    def ajouter_ville(self, ville):
        self.villes.append(ville)

    def enlever_ville(self, ville):
        self.villes.remove(ville)

    def __init__():
        villes = []
        for i in range(10):
            villes.append(Ville("Ville " + str(i), random.randint(0, 100), random.randint(0, 100)))
        return Region(villes)
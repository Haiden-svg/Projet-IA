from Region import *
from Ville import *
import random
class Route:
    def __init__(self):
        self.villes = []
        self.poids = 0

    def ajouter_ville(self, ville):
        self.villes.append(ville)
        self.poids +=ville.distance_vers(self.villes[-2])

    def __str__(self):
        return f"Route: {self.villes}, Poids: {self.poids}"


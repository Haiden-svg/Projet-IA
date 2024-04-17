from Region import *
from Ville import *
import random
class Route:
    def __init__(self):
        self.cities = []
        self.weight = 0

    def ajouter_ville(self, ville):
        self.cities.append(city)
        self.weight += weight

    def __str__(self):
        return f"Route: {self.cities}, Poids: {self.weight}"


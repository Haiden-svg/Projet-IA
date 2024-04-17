from Region import *
from Ville import *
import random
class Route:
    def __init__(self):
        self.cities = []
        self.weight = 0

    def add_city(self, city, weight):
        self.cities.append(city)
        self.weight += weight

    def __str__(self):
        return f"Route: {self.cities}, Poids: {self.weight}"
    
    def parcourir(self, region):
        for i in range(len(region.villes)):
            if i == len(region.villes) - 1:
                self.add_city(region.villes[i], region.villes[i].distance_vers(region.villes[0]))
            else:
                self.add_city(region.villes[i], region.villes[i].distance_vers(region.villes[i+1]))
        print(self)
        return self
    


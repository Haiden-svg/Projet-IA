from Region import *
from Route import *
from Ville import *

class Main:
    def __init__(self):
        self.villes = [Ville("Paris", 0, 0), Ville("Lyon", 10, 0), Ville("Marseille", 0, 10), Ville("Nice", 10, 10)]
        self.region = Region(self.villes)
        self.route = Route()

    def run(self):
        self.region.afficher_villes()
        self.route.add_city(self.villes[0], 0)
        self.route.add_city(self.villes[1], 10)
        self.route.add_city(self.villes[2], 10)
        self.route.add_city(self.villes[3], 10)
        print(self.route.weight)
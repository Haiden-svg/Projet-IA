import random
from Region import *
from Ville import *
from Route import *

class ListeRoute:

    def __init__(self):
        self.routes = []

    def crossover(route1, route2):
        # Choisissez un point d'index aléatoire
        index = random.randint(1, len(route1.villes) - 1)

        # Créez les premières moitiés des nouvelles routes
        new_route1_villes = route1.villes[:index]
        new_route2_villes = route2.villes[:index]

        # Ajoutez les villes manquantes à la fin des nouvelles routes
        new_route1_villes += [ville for ville in route2.villes if ville not in new_route1_villes]
        new_route2_villes += [ville for ville in route1.villes if ville not in new_route2_villes]

        # Créez les nouvelles routes
        new_route1 = Route()
        new_route1.ajouter_villes(new_route1_villes)
        new_route2 = Route()
        new_route2.ajouter_villes(new_route2_villes)

        return new_route1, new_route2
    
    def add_route(self, route):
        self.routes.append(route)

    def remove_route(self, route):
        self.routes.remove(route)

    def get_routes(self):
        return self.routes

    def clear_routes(self):
        self.routes = []

    def print_routes(self):
        print("====================================")
        for route in self.routes:
            
            print(route)
            print("====================================")

    def trier_routes(self):
        self.routes.sort(key=lambda x: x.poids)
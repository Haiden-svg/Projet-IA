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
    
    def evolutive_list_route(self,list):
        for i in range(50):
            # Sélectionnez deux routes parentes
            parent1 = list.routes[i]
            parent2 = list.routes[i+1]

            # Effectuez le croisement
            child1, child2 = self.crossover(parent1, parent2)

            # Ajoutez les enfants à la liste des routes
            list.add_route(child1)
            list.add_route(child2)

        # Triez les routes par poids
        list.trier_routes()

        # Ne gardez que les 50 meilleures routes
        list.routes = list.routes[:50]

        # Affichez les routes
        list.print_routes()
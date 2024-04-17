from Ville import *
import random
class Region:
    def __init__(self, villes):
        self.villes = villes

    def __init__(self):
        self.villes = []
        for i in range(10):
            self.villes.append(Ville("Ville " + str(i), random.randint(0, 100), random.randint(0, 100)))

    def afficher_villes(self):
        for ville in self.villes:
            print(ville)

    def ajouter_ville(self, ville):
        self.villes.append(ville)

    def enlever_ville(self, ville):
        self.villes.remove(ville)
        
    def selection_tournoi(self, taille_tournoi):
        meilleur = None
        for i in range(taille_tournoi):
            individu = random.choice(self.routes)
            if meilleur is None or individu.distance_totale() < meilleur.distance_totale():
                meilleur = individu
        return meilleur

    def croisement_ordre(self, parent1, parent2):
        taille = len(parent1.villes)

        # Choisissez une sous-séquence de la route du parent1
        debut = random.randint(0, taille - 1)
        fin = random.randint(debut, taille)

        # Copiez la sous-séquence dans l'enfant
        enfant_villes = parent1.villes[debut:fin]

        # Remplissez le reste de la route avec les villes du parent2
        for ville in parent2.villes:
            if ville not in enfant_villes:
                enfant_villes.append(ville)

        return Route(enfant_villes)
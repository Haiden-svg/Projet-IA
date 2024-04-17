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

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
class Graphics:
    def __init__(self): # Constructeur
        self.fig, self.ax = plt.subplots()

    def draw_cities(self, cities, img_path): # Dessine les villes
        img = plt.imread(img_path)
        imagebox = OffsetImage(img, zoom=0.1)
        
        for city in cities: # Pour chaque ville dans la liste des villes
            ab = AnnotationBbox(imagebox, (city.x, city.y))
            self.ax.add_artist(ab) # Ajoute la ville au graphique

    def draw_route(self, route): # Dessine la route
        x = [city.x for city in route.villes] # Liste des coordonnees x des villes
        y = [city.y for city in route.villes] # Liste des coordonnees y des villes
        self.ax.plot(x + [x[0]], y + [y[0]], 'b-')  # 'b-' signifie une ligne bleue

    def show(self):
        plt.show() # Affiche le graphique

    def update(self, route): # Met a jour le graphique
        self.ax.clear() # Efface le graphique
        self.draw_cities(route.villes, 'img/ville.png') # Dessine les villes
        self.draw_route(route) # Dessine la route
        plt.draw()
        plt.pause(0.5)  # Pause pour permettre la mise à jour du graphique
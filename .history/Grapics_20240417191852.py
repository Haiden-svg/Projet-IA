import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
class Graphics:
    def __init__(self, background_img_path):
        self.fig, self.ax = plt.subplots()
        self.background_img = plt.imread(background_img_path)
        self.ax.imshow(self.background_img)

    def draw_cities(self, cities, img_path):
        img = plt.imread(img_path)
        imagebox = OffsetImage(img, zoom=0.1)
        
        for city in cities:
            ab = AnnotationBbox(imagebox, (city.x, city.y))
            self.ax.add_artist(ab)

    def draw_route(self, route):
        x = [city.x for city in route.villes]
        y = [city.y for city in route.villes]
        self.ax.plot(x + [x[0]], y + [y[0]], 'b-')  # 'b-' signifie une ligne bleue

    def show(self):
        plt.show()

    def update(self, route):
        self.ax.clear()
        self.draw_cities(route.villes, 'img/ville.png')
        self.draw_route(route)
        plt.draw()
        plt.pause(0.5)  # Pause pour permettre la mise à jour du graphique
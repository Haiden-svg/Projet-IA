import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class Graphics:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

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
import matplotlib.pyplot as plt

class Graphics:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw_cities(self, cities):
        x = [city.x for city in cities]
        y = [city.y for city in cities]
        self.ax.scatter(x, y)

    def draw_route(self, route):
        x = [city.x for city in route.villes]
        y = [city.y for city in route.villes]
        self.ax.plot(x + [x[0]], y + [y[0]], 'b-')  # 'b-' signifie une ligne bleue

    def show(self):
        plt.show()
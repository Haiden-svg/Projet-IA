class Route:
    def __init__(self):
        self.cities = []
        self.weight = 0

    def add_city(self, city, weight):
        self.cities.append(city)
        self.weight += weight

    def distance_totale(self):
        return sum(self.villes[i].distance(self.villes[i+1]) for i in range(len(self.villes)-1))

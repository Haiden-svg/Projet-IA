class Route:
    def __init__(self):
        self.cities = []
        self.weight = 0

    def add_city(self, city, weight):
        self.cities.append(city)
        self.weight += weight

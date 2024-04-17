class Ville:
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ville: {self.nom}, Coordonnées: ({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

    def distance_vers(self, autre_ville):
        distance_x = abs(self.x - autre_ville.x)
        distance_y = abs(self.y - autre_ville.y)
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5
        return distance
    

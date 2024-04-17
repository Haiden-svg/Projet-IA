class ListeRoute:
    def __init__(self):
        self.routes = []

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
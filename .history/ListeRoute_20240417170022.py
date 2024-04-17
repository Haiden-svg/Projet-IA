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
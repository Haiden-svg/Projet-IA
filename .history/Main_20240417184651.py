from Region import *
from Route import *
from Ville import *
from Voyageur import *
from ListeRoute import *
from Grapics import *
class Main:
    france = Region()
    france.ajouter_ville(Ville("Ville1",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville2",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville3",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville4",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville5",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville6",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville7",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville8",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville9",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville10",random.randint(0,100),random.randint(0,100) ))
    jean = Voyageur(france)
    list=ListeRoute()
    for i in range(100):
        route=Route()
        route.ajouter_villes(jean.voyager())
        list.add_route(route)
    list.evolutive_list_route(100)
    #list.print_routes()
    graphics = Graphics()
    graphics.draw_cities(france.villes)
    meilleure_route = list.routes[0]
    graphics.draw_route(meilleure_route)
    graphics.show()    
    

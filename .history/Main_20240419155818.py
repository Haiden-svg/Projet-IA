from Region import *
from Route import *
from Ville import *
from Voyageur import *
from ListeRoute import *
from Grapics import *
class Main:
    france = Region() # Creez une region

    # Ajoutez des villes a la region
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
    france.ajouter_ville(Ville("Ville11",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville12",random.randint(0,100),random.randint(0,100) ))
    france.ajouter_ville(Ville("Ville13",random.randint(0,100),random.randint(0,100) ))

    # Creez un voyageur
    jean = Voyageur(france)
    list=ListeRoute()
    # Creez 100 routes
    for i in range(100):
        route=Route()
        route.ajouter_villes(jean.voyager())
        list.add_route(route)
   
   # Creez une fenetre graphique
    graphics = Graphics()
    graphics.draw_cities(france.villes, 'img/ville.png')
    # Boucle d'evolution
    for generation in range(10):
        list.evolutive_list_route(100)
        meilleure_route = list.routes[0]
        graphics.update(meilleure_route)

    graphics.show()
    # Affichez les routes
    list.print_routes()

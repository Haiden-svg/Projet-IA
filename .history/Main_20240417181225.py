from Region import *
from Route import *
from Ville import *
from Voyageur import *
from ListeRoute import *
class Main:
    france = Region()
    france.ajouter_ville(Ville("Ville1",10,0 ))
    france.ajouter_ville(Ville("Ville2",0,10 ))
    france.ajouter_ville(Ville("Ville3",100,0 ))
    france.ajouter_ville(Ville("Ville4",50,50 ))
    france.ajouter_ville(Ville("Ville5",75,75 ))
    france.ajouter_ville(Ville("Ville6",90,90 ))
    france.ajouter_ville(Ville("Ville7",60,60 ))
    france.ajouter_ville(Ville("Ville8",70,70 ))
    france.ajouter_ville(Ville("Ville9",30,30 ))
    france.ajouter_ville(Ville("Ville10",10,10 ))
    jean = Voyageur(france)
    route=Route()
    route.ajouter_villes(jean.voyager())
    list=ListeRoute()
    for i in range(100):
        route=Route()
        route.ajouter_villes(jean.voyager())
        list.add_route(route)
    #list.print_routes()
    #list.trier_routes()
    #list.print_routes() 
    list.evolutive_list_route(100)
    #list.print_routes()
    

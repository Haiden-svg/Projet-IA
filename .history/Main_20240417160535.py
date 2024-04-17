from Region import *
from Route import *
from Ville import *

class Main:
    paris = Ville("Paris", 0, 0)
    france = Region([paris])
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
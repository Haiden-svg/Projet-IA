from Region import *
from Route import *
from Ville import *

class Main:
    paris = Ville("Paris", 0, 0)
    france = Region()
    france.ajouter_ville(Ville("Ville1", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville2", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville3", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville4", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville5", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville6", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville7", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville8", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville9", random.randint(0, 100), random.randint(0, 100)))
    france.ajouter_ville(Ville("Ville10", random.randint(0, 100), random.randint(0, 100)))
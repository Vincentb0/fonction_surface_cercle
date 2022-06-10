"""
Fonction qui permet de calculer la surface (l'aire) d'un cercle
dont on lui fourni le rayon en argument.

surface_cercle(rayon):

Calcul de la surface d'un cercle : A = pi * r²
"""
from math import *

def surface_cercle(rayon):
    aire = round(pi * pow(rayon, 2), 5)
    return aire


print("Entrez le rayon d'un cercle en cm :", end=" ")
r = eval(input())
surface = surface_cercle(r)
print("l'aire est égale à :", surface, "cm²")
# ou
# print("l'aire est égale à :", surface_cercle(r), "cm²")

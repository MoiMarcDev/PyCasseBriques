""" Constantes / paramètres / variables à utiliser "globalement" """
import os

from Element import ElementList

dossier_racine:str = os.path.dirname(__file__)
dossier_niveau:str = os.path.join(dossier_racine, "niveau")
dossier_img:str = os.path.join(dossier_racine, "img")
dossier_csv:str = os.path.join(dossier_racine, "csv")

_fichier_csv_element = os.path.join(dossier_csv, "element.csv")
elements:ElementList = ElementList(_fichier_csv_element)

# On représente un niveau par une grille sans laquelle des éléments sont positionnés (comme les murs, les briques)
# La grille (ou tableau) a une delargeur de 28 "cases" et une hauteur de 27 "cases" (soit 756 cases au total)
# Chaque élément (mur, brique) est positionné à un emplacement de la grille
# Cet emplacement correspont au point en haut à gauche de l'élément
niveau_grille_largeur, niveau_grille_hauteur = 28,27
""" Constantes / paramètres / variables à utiliser "globalement" """
import os

dossier_racine = os.path.dirname(__file__)
dossier_niveau = os.path.join(dossier_racine, "niveau")
dossier_img = os.path.join(dossier_racine, "img")
dossier_csv = os.path.join(dossier_racine, "csv")

fichier_csv_element = os.path.join(dossier_csv, "element.csv")

# On représente un niveau par une grille sans laquelle des éléments sont positionnés (comme les murs, les briques)
# La grille (ou tableau) a une delargeur de 28 "cases" et une hauteur de 27 "cases" (soit 756 cases au total)
# Chaque élément (mur, brique) est positionné à un emplacement de la grille
# Cet emplacement correspont au point en haut à gauche de l'élément
niveau_grille_largeur, niveau_grille_hauteur = 28,27
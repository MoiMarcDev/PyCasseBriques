""" Constantes / paramètres / variables à utiliser "globalement" """
import os

import pygame

from Element import ElementList

# Dossiers
nom_dossier_racine:str = os.path.dirname(__file__)
nom_dossier_img:str = os.path.join(nom_dossier_racine, "img")
nom_dossier_csv:str = os.path.join(nom_dossier_racine, "csv")
# Fond
surface_image_fond = pygame.image.load(os.path.join(nom_dossier_img, "fond.png"))
# Mur
surface_image_mur = pygame.image.load(os.path.join(nom_dossier_img, "mur.png"))
mur_epaisseur = surface_image_mur.get_width()
# Balle
surface_balle = pygame.image.load(os.path.join(nom_dossier_img, "balle.png"))
# Fenetre
fenetre_dimension = (surface_image_fond.get_width() + 150, surface_image_fond.get_height())
fenetre_titre = "pyCasseBriques"
# Elements possibles (briques à casser) pour les plateaux de jeu
_nom_fichier_csv_element = os.path.join(nom_dossier_csv, "element.csv")
elements:ElementList = ElementList(_nom_fichier_csv_element)
# Temps de pause en millisecondes entre chaqued déplacement de la balle, de la raquette, ...
jeu_delai_pause_ms = 3
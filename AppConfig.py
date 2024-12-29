""" Constantes / paramètres / variables à utiliser "globalement" """
import os

import pygame

from Element import ElementList

nom_dossier_racine:str = os.path.dirname(__file__)
nom_dossier_img:str = os.path.join(nom_dossier_racine, "img")
nom_dossier_csv:str = os.path.join(nom_dossier_racine, "csv")

_nom_fichier_csv_element = os.path.join(nom_dossier_csv, "element.csv")
elements:ElementList = ElementList(_nom_fichier_csv_element)

surface_image_fond = pygame.image.load(os.path.join(nom_dossier_img, "fond.png"))
surface_balle = pygame.image.load(os.path.join(nom_dossier_img, "balle.png"))

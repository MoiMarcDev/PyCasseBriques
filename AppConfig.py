""" Constantes / paramètres / variables à utiliser "globalement" """
import os

import pygame

from Element import ElementList

# Dossiers
nom_dossier_racine:str = os.path.dirname(__file__)
nom_dossier_img:str = os.path.join(nom_dossier_racine, "img")
nom_dossier_csv:str = os.path.join(nom_dossier_racine, "csv")
nom_dossier_son:str = os.path.join(nom_dossier_racine, "son")
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
# Sons
nom_fichier_son_contact = os.path.join(nom_dossier_son, "contact.wav")
nom_fichier_son_debut_jeu = os.path.join(nom_dossier_son, "debut_jeu.wav")
nom_fichier_son_destruction = os.path.join(nom_dossier_son, "destruction.wav")
# Temps de pause en millisecondes entre chaqued déplacement de la balle, de la raquette, ...
jeu_delai_pause_ms = 3
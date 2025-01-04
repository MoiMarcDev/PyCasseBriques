""" Constantes / paramètres / variables à utiliser "globalement" """
import os

import pygame

from Element import ElementList

"""Dossiers"""
nom_dossier_racine:str = os.path.dirname(__file__)
nom_dossier_img:str = os.path.join(nom_dossier_racine, "img")
nom_dossier_csv:str = os.path.join(nom_dossier_racine, "csv")
nom_dossier_son:str = os.path.join(nom_dossier_racine, "son")

"""Fond"""
fond_surface = pygame.image.load(os.path.join(nom_dossier_img, "fond.png"))
fond_largeur = fond_surface.get_width()
fond_hauteur = fond_surface.get_height()

"""Mur"""
mur_surface = pygame.image.load(os.path.join(nom_dossier_img, "mur.png"))
mur_epaisseur = mur_surface.get_width()

"""Elements"""
# Elements possibles (briques à casser) pour les plateaux de jeu
_nom_fichier_csv_element = os.path.join(nom_dossier_csv, "element.csv")
elements:ElementList = ElementList(_nom_fichier_csv_element)

"""Raquette"""
raquette_surface = elements.get_element("RAQUETTE").surfaces[0]
raquette_hauteur = raquette_surface.get_height()
raquette_largeur = raquette_surface.get_width()
raquette_x_min = mur_epaisseur
raquette_x_max = fond_largeur - mur_epaisseur - raquette_largeur

# Raquette, effet (en dégré) sur l'angle de la balle si la raquette est en mouvement lors du contact avec la balle
raquette_mouvement_effet_angle_direction_balle = 30

"""Balle"""
balle_surface = pygame.image.load(os.path.join(nom_dossier_img, "balle.png"))
# Dimensions (du rectangle englobant)
balle_largeur = balle_surface.get_width()
balle_hauteur = balle_surface.get_height()
# Angles mini et maxi possible pour les déplacement de la balle dans la partie supérieure et dans la partie inférieure
balle_angles_autorises = ((10, 170), (190, 350))
# Top et left mini et maxi pour la balle (=pour l'angle haut gauche du rectangle englobant)
balle_x_min = mur_epaisseur
balle_x_max = fond_largeur - mur_epaisseur
balle_y_min = mur_epaisseur
balle_y_max = fond_hauteur - raquette_hauteur - balle_hauteur

"""Fenetre"""
fenetre_dimension = (fond_surface.get_width() + 200, fond_surface.get_height())
fenetre_titre = "pyCasseBriques"

"""Sons"""
nom_fichier_son_balle_perdue = os.path.join(nom_dossier_son, "balle_perdue.wav")
nom_fichier_son_contact = os.path.join(nom_dossier_son, "contact.wav")
nom_fichier_son_debut_jeu = os.path.join(nom_dossier_son, "debut_jeu.wav")
nom_fichier_son_destruction = os.path.join(nom_dossier_son, "destruction.wav")

"""Jeu"""
# Temps de pause en millisecondes entre chaqued déplacement de la balle, de la raquette, ...
jeu_delai_pause_ms = 3
jeu_surface = pygame.display.set_mode(fenetre_dimension, pygame.DOUBLEBUF)

"""
Niveau (plateau de jeu)
"""
import os
import AppConfig

import pygame

from Grille import Grille, GrilleItem

class NiveauPlateau:
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier:str):
        self._ecran = ecran
        self._nom_fichier:str = nom_fichier
        self._grille_depart:Grille = Grille( self._nom_fichier )
        
    def display(self):
        """Affichage initial selon la grille"""
        for gi in self._grille_depart:
            px:int = 30*gi.x
            py:int = 30*gi.y
            sf = AppConfig.elements.get_surface(gi.element.identifiant)
            self._ecran.blit(sf, (px, py))

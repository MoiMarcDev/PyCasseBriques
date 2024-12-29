"""
Niveau (plateau de jeu)
"""
import AppConfig

import pygame

from Element import ElementItem
from Grille import Grille

class AireDeJeu:
   
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier:str):
        self._ecran:pygame.surface.Surface = ecran
        self._nom_fichier:str = nom_fichier
        self._grille_depart:Grille = Grille( self._nom_fichier )
        self._raquette:ElementItem = AppConfig.elements.get_element("RAQUETTE")
        self._raquette_vitesse:int = 1
        self._raquette_largeur = self._raquette.surfaces[0].get_width()
        # Ci-après : serait, normalement, à calculer, notamment en fonction de la position des murs
        self._raquette_x_min:int = 30
        self._raquette_x_max:int = 809
        self._raquette_x:int = 360
        self._raquette_y:int = 780 # N'est pas supposé changer ! Sauf peut-être une future version du jeu ?
        
    def afficher(self):
        """
        Affichage initial selon la grille
        Chaque élément (mur, brique) est positionné à un emplacement de la grille (coordonées x et y)
        """
        # Raquette
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        # Éléménts du décor (mur, briques à casser)
        for item in self._grille_depart:
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            self._ecran.blit(sf, (item.x, item.y))

    def deplacer_raquette(self, delta_x:int):
        if delta_x < 0 and self._raquette_x <= self._raquette_x_min: return # ignoré (déjà bord gauche)
        if delta_x > 0 and self._raquette_x + self._raquette_largeur >= self._raquette_x_max: return # ignoré (déjà bord droite)
        
        self._raquette_x += (self._raquette_vitesse * delta_x)
        
        self._raquette_x = max(self._raquette_x_min, self._raquette_x)
        self._raquette_x = min(self._raquette_x, self._raquette_x_max - self._raquette_largeur)
        
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))

"""
Niveau (plateau de jeu)
"""
import AppConfig

import pygame

from Element import ElementItem
from Grille import Grille

class AireDeJeu:
   
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier:str):
        self._fond:pygame.surface.Surface = AppConfig.surface_image_fond # Pourrait être rendu paramétrable dans une future version ?
        self._ecran:pygame.surface.Surface = ecran
        self._nom_fichier:str = nom_fichier
        self._grille_depart:Grille = Grille( self._nom_fichier )
        self._raquette:ElementItem = AppConfig.elements.get_element("RAQUETTE")
        self._raquette_largeur = self._raquette.surfaces[0].get_width()
        self._raquette_hauteur = self._raquette.surfaces[0].get_height()
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
        # Fond
        self._ecran.blit(AppConfig.surface_image_fond, (0, 0))
        # Raquette
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        # Éléménts du décor (mur, briques à casser)
        for item in self._grille_depart:
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            self._ecran.blit(sf, (item.x, item.y))

    def deplacer_raquette(self, delta_x:int):
        if delta_x < 0 and self._raquette_x <= self._raquette_x_min: return # ignoré (déjà bord gauche)
        if delta_x > 0 and self._raquette_x + self._raquette_largeur >= self._raquette_x_max: return # ignoré (déjà bord droite)
        
        nouveau_x = self._raquette_x + delta_x
        
        nouveau_x = max(self._raquette_x_min, nouveau_x)
        nouveau_x = min(nouveau_x, self._raquette_x_max - self._raquette_largeur)
        
        if self._raquette_x == nouveau_x: return
        
        # Récupération du fond pour écraser l'actuelle zone occupée par la raquette
        rect_arriere_plan = pygame.Rect(self._raquette_x, self._raquette_y, self._raquette_largeur, self._raquette_hauteur)
        surf_arriere_plan = self._fond.subsurface(rect_arriere_plan)
        self._ecran.blit( surf_arriere_plan, (self._raquette_x, self._raquette_y))
        # Nouvel position de la raquette et affichage
        self._raquette_x = nouveau_x
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))

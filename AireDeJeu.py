"""
Niveau (plateau de jeu)
"""
import AppConfig

import pygame

from Element import ElementItem
from Grille import Grille

class AireDeJeu:
    # On représente un niveau par une grille sans laquelle des éléments sont positionnés (comme les murs, les briques)
    # La grille (ou tableau) a une delargeur de 28 "cases" et une hauteur de 27 "cases" (soit 756 cases au total)
    # Chaque "case" a une résolutionde 30x30 pixels
    largeur_x:int = 28
    hauteur_y:int = 27
    resolution_case:int = 30
    raquette_px_min:int = resolution_case
    raquette_px_max:int = ((largeur_x-1) * resolution_case) - 1
    
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier:str):
        self._ecran:pygame.surface.Surface = ecran
        self._nom_fichier:str = nom_fichier
        self._grille_depart:Grille = Grille( self._nom_fichier )
        self._raquette:ElementItem = AppConfig.elements.get_element("RAQUETTE")
        self._raquette_px:int = AireDeJeu.resolution_case * 12
        self._raquette_py:int = AireDeJeu.resolution_case * (AireDeJeu.hauteur_y - 1) # N'est pas supposé changer ! Sauf peut-être une future version du jeu ?
        self._raquette_vitesse:int = 1
        self._raquette_largeur_px = self._raquette.largeur * AireDeJeu.resolution_case
        
    def display(self):
        """
        Affichage initial selon la grille
        Chaque élément (mur, brique) est positionné à un emplacement de la grille (coordonées x et y)
        """
        for item in self._grille_depart:
            px:int = AireDeJeu.resolution_case*item.x
            py:int = AireDeJeu.resolution_case*item.y
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            self._ecran.blit(sf, (px, py))
        
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_px, self._raquette_py))

    def deplacer_raquette(self, delta_x:int):
        if delta_x < 0 and self._raquette_px <= AireDeJeu.raquette_px_min: return # ignoré (déjà bord gauche)
        if delta_x > 0 and self._raquette_px + self._raquette_largeur_px >= AireDeJeu.raquette_px_max: return # ignoré (déjà bord droite)
        
        self._raquette_px += (self._raquette_vitesse * delta_x)
        
        self._raquette_px = max( AireDeJeu.raquette_px_min, self._raquette_px)
        self._raquette_px = min( AireDeJeu.raquette_px_max, self._raquette_px - self._raquette_largeur_px)
        
        self._ecran.blit( self._raquette.surfaces[0], (self._raquette_px, self._raquette_py))

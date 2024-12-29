"""
Niveau (plateau de jeu)
"""
import random

import pygame

import AppConfig
from Element import ElementItem
from Grille import Grille

class AireDeJeu:
   
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier_contenu_aire:str):
        """Écran"""
        self._ecran_surface:pygame.surface.Surface = ecran
        """Fond"""
        # Pourrait être rendu paramétrable dans une future version
        self._fond_surface:pygame.surface.Surface = AppConfig.surface_image_fond 
        """Grille"""
        # Contenu initial de l'aire = éléments = mur et briques
        self._nom_fichier_contenu_aire:str = nom_fichier_contenu_aire
        self._grille_depart:Grille = Grille( self._nom_fichier_contenu_aire )
        """Raquette"""
        self._raquette:ElementItem = AppConfig.elements.get_element("RAQUETTE")
        self._raquette_largeur = self._raquette.surfaces[0].get_width()
        self._raquette_hauteur = self._raquette.surfaces[0].get_height()
        # Ci-après : serait, normalement, à calculer, notamment en fonction de la position des murs
        self._raquette_x_min:int = 30
        self._raquette_x_max:int = 809
        self._raquette_x:int = 360
        self._raquette_y:int = 780 # N'est pas supposé changer ! Sauf peut-être une future version du jeu ?
        """Balle"""
        # Pourrait être rendu paramétrable dans une future version
        self._balle_surface:pygame.surface.Surface = AppConfig.surface_balle 
        # Position initiale aléatoire sur la raquette (décalage par rapport au centre de la raquette, à gauche ou à droite, aléatoirement)
        # Décalage de 1/8 de la largeur de la raquete auquel on ajoute aléatoirement jusqu'à 1/4 de la largeur de la raquette
        balle_delta_x:int = ( self._raquette_largeur // 8 ) + random.randint(0, self._raquette_largeur) // 4
        if random.randint(0,100) < 50: balle_delta_x = -1 * balle_delta_x
        self._balle_x = self._raquette_x + ( self._raquette_largeur // 2 ) + balle_delta_x
        self._balle_y = self._raquette_y - self._balle_surface.get_height()
        self._balle_largeur = self._balle_surface.get_width()
        self._balle_hauteur = self._balle_surface.get_height()
        
    def afficher(self):
        """
        Affichage initial selon la grille
        Chaque élément (mur, brique) est positionné à un emplacement de la grille (coordonées x et y)
        """
        # Fond
        self._ecran_surface.blit(AppConfig.surface_image_fond, (0, 0))
        # Éléménts du décor (mur, briques à casser)
        for item in self._grille_depart:
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            self._ecran_surface.blit(sf, (item.x, item.y))
        pygame.display.flip()
        # Raquette
        self._ecran_surface.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        # Balle
        self._ecran_surface.blit( self._balle_surface, (self._balle_x, self._balle_y))
        # Affichage 
        pygame.display.update()

    def deplacer_balle(self, x:int, y:int=0):
        """Déplacer la balle"""
        # Remettre le fond
        self._restaurer_fond(self._balle_x, self._balle_y, self._balle_largeur, self._balle_hauteur)
        # Afficher à la nouvelle position
        self._balle_x += x
        self._balle_y += y
        self._ecran_surface.blit( self._balle_surface, (self._balle_x, self._balle_y))
        pygame.display.update((self._balle_x, self._balle_y,self._balle_largeur, self._balle_hauteur))
        
    def deplacer_raquette(self, delta_x:int, balle_lancee:bool):
        """Déplacer la raquette et, éventuellement, la balle si pas encore lancée et donc toujours 'posée' sur la raquette"""
        if delta_x < 0 and self._raquette_x <= self._raquette_x_min: return # ignoré (déjà bord gauche)
        if delta_x > 0 and self._raquette_x + self._raquette_largeur >= self._raquette_x_max: return # ignoré (déjà bord droite)
        
        nouveau_x = self._raquette_x + delta_x
        
        nouveau_x = max(self._raquette_x_min, nouveau_x)
        nouveau_x = min(nouveau_x, self._raquette_x_max - self._raquette_largeur)
        
        if self._raquette_x == nouveau_x: return
        
        # Si la balle est posée sur la raquette, c'est à dire si elle n'a pas été lancée, alors elle doit bouger avec la raquette        
        if not balle_lancee: 
            self.deplacer_balle(nouveau_x - self._raquette_x)
        # Récupération du fond pour écraser l'actuelle zone occupée par la raquette
        self._restaurer_fond(self._raquette_x, self._raquette_y, self._raquette_largeur, self._raquette_hauteur)
        # Nouvelle position de la raquette et affichage
        self._raquette_x = nouveau_x
        self._ecran_surface.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        pygame.display.update((self._raquette_x, self._raquette_y,self._raquette_largeur, self._raquette_hauteur))
        
    def _restaurer_fond(self, x:int, y:int, largeur:int, hauteur:int)        :
        rect_arriere_plan = pygame.Rect(x, y, largeur, hauteur)
        surf_arriere_plan = self._fond_surface.subsurface(rect_arriere_plan)
        self._ecran_surface.blit(surf_arriere_plan, (x, y))
        pygame.display.update((x, y, largeur, hauteur))

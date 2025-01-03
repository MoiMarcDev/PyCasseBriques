"""
Niveau (plateau de jeu)
"""
import math
import random

import pygame

import AppConfig
from Element import ElementItem
from Grille import Grille

class AireDeJeu:
   
    def __init__(self, ecran:pygame.surface.Surface, nom_fichier_contenu_aire:str):
        """Écran"""
        self._surface_ecran:pygame.surface.Surface = ecran
        """Fond"""
        # Pourrait être rendu paramétrable dans une future version
        self._surface_fond:pygame.surface.Surface = AppConfig.surface_image_fond 
        """Grille"""
        # Contenu initial de l'aire = éléments = mur et briques
        self._nom_fichier_contenu_aire:str = nom_fichier_contenu_aire
        self._grille:Grille = Grille( self._nom_fichier_contenu_aire )
        """Raquette"""
        self._raquette:ElementItem = AppConfig.elements.get_element("RAQUETTE")
        self._raquette_largeur:int = self._raquette.surfaces[0].get_width()
        self._raquette_hauteur:int = self._raquette.surfaces[0].get_height()
        self._raquette_x_min:int = AppConfig.mur_epaisseur
        self._raquette_x_max:int = AppConfig.surface_image_fond.get_width() - AppConfig.mur_epaisseur
        self._raquette_x:int = (AppConfig.surface_image_fond.get_width() - self._raquette_largeur) // 2
        self._raquette_y:int = AppConfig.surface_image_fond.get_height() - self._raquette_hauteur
        """Balle"""
        # Pourrait être rendu paramétrable dans une future version
        self._balle_surface:pygame.surface.Surface = AppConfig.surface_balle.convert_alpha()
        # Position initiale aléatoire sur la raquette (décalage par rapport au centre de la raquette, à gauche ou à droite, aléatoirement)
        # Décalage de 1/8 de la largeur de la raquete auquel on ajoute aléatoirement jusqu'à 1/4 de la largeur de la raquette
        balle_delta_x:int = ( self._raquette_largeur // 8 ) + random.randint(0, self._raquette_largeur) // 6
        if random.randint(0,100) < 50: balle_delta_x = -1 * balle_delta_x
        self._balle_x:float = self._raquette_x + ( self._raquette_largeur // 2 ) + balle_delta_x
        self._balle_y:float = self._raquette_y - self._balle_surface.get_height() - 1
        self._balle_x_origine:int|None = None
        self._balle_y_origine:int|None = None
        self._balle_largeur:int = self._balle_surface.get_width()
        self._balle_hauteur:int = self._balle_surface.get_height()
        self._balle_mouvement_angle:float = \
            self._get_angle_depuis_adjacent(balle_delta_x) if balle_delta_x >=0 else 90.0 + self._get_angle_depuis_oppose(-1 * balle_delta_x)
        self._balle_mouvement_x_y = self._get_mouvement_x_y()
        
    def _get_angle_depuis_adjacent(self, adja:float, hypo:float|None=None)->float:
        """Retourne un angle en degrés à partir de la longueur de l'hypoténuse et de la longueur du coté adjacent"""
        if hypo is None: hypo = 0.5 * self._raquette_largeur
        return math.acos(adja/hypo) * 180 / math.pi

    def _get_angle_depuis_oppose(self, oppo:float, hypo:float|None=None)->float:
        """Retourne un angle en degrés à partir de la longueur de l'hypoténuse et de la longueur du coté adjacent"""
        if hypo is None: hypo = 0.5 * self._raquette_largeur
        return math.asin(oppo/hypo) * 180 / math.pi

    def _get_mouvement_x_y(self,angle_degre:int|None=None) -> list[float]:
        """
        Retourne le déplacement x et y pour un angle de balle donné.
        Ceci en tenant compte de l'orientation propre à pigame (repère avec l'origine en haut à gauche, x croissant de gauche à droite, y croissant de haut en bas)
        """
        if angle_degre is None: angle_degre = self._balle_mouvement_angle
        
        if 0 == angle_degre or 360==angle_degre: return (1,0)
        if 90 == angle_degre: return(0,1)
        if 180 == angle_degre: return (-1,0)
        if 270 == angle_degre: return (0,-1)

        if angle_degre<90:      # 0-90
            angle_radian = math.radians( angle_degre )
            return math.cos(angle_radian), -math.sin(angle_radian)
        if angle_degre<180:     # 90-180
            angle_radian = math.radians( angle_degre -90 )
            return -math.sin(angle_radian), -math.cos(angle_radian)
        if angle_degre<270:     # 180-270
            angle_radian = math.radians( angle_degre - 180 )
            return -math.cos(angle_radian), math.sin(angle_radian)
        if angle_degre<360:     # 270-360
            angle_radian = math.radians( angle_degre - 270 )
            return math.sin(angle_radian), math.cos(angle_radian)
        
        raise Exception(f"Angle incorrect: {angle_degre}")

    def afficher(self):
        """
        Affichage initial selon la grille
        Chaque élément (mur, brique) est positionné à un emplacement de la grille (coordonées x et y)
        """
        # Fond
        self._surface_ecran.blit(AppConfig.surface_image_fond, (0, 0))
        # Mur
        for x in range(0, AppConfig.surface_image_fond.get_width() // AppConfig.mur_epaisseur):
            self._surface_ecran.blit(AppConfig.surface_image_mur, (x*AppConfig.mur_epaisseur, 0))
        for y in range(0, AppConfig.surface_image_fond.get_height() // AppConfig.mur_epaisseur):
            self._surface_ecran.blit(AppConfig.surface_image_mur, (0, y*AppConfig.mur_epaisseur))
            self._surface_ecran.blit(AppConfig.surface_image_mur, (x*AppConfig.mur_epaisseur, y*AppConfig.mur_epaisseur))
        # Éléménts du décor (briques à casser)
        for item in self._grille:
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            self._surface_ecran.blit(sf, (item.x, item.y))
        pygame.display.flip()
        # Raquette
        self._surface_ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        # Balle
        self._surface_ecran.blit( self._balle_surface, (self._balle_x, self._balle_y))
        # Affichage 
        pygame.display.update()

    def deplacer_balle(self, force_x_y:list[float]|None=None):
        """Déplacer la balle"""
        x_y = self._balle_mouvement_x_y if force_x_y is None else force_x_y
        nouveau_x:float = self._balle_x + x_y[0]
        nouveau_y:float = self._balle_y + x_y[1]
        # Déplacement / pixels ?
        if int(nouveau_x) != int(self._balle_x) or int(nouveau_y) != int(self._balle_y):
            if abs(int(self._balle_x) - int(nouveau_x) ) > 1: raise Exception("Déplacement X > 1")
            if abs(int(self._balle_y) - int(nouveau_y) ) > 1: raise Exception("Déplacement Y > 1")
            # Remettre le fond
            self._restaurer_fond(self._balle_x, self._balle_y, self._balle_largeur, self._balle_hauteur)
            # Afficher à la nouvelle position
            self._surface_ecran.blit( self._balle_surface, (int(nouveau_x), int(nouveau_y)))
            pygame.display.update((int(nouveau_x), int(nouveau_y),self._balle_largeur, self._balle_hauteur))

        # Nouvelle position
        self._balle_x_origine, self._balle_y_origine = int(self._balle_x), int(self._balle_y)
        self._balle_x, self._balle_y = nouveau_x, nouveau_y

        """Contact ?"""
        balle_rect = pygame.Rect(int(self._balle_x), int(self._balle_y), self._balle_largeur, self._balle_hauteur)
        
        # La balle est-elle au contact d'un mur ? d'une brique ?
        contact_face:str = None
        if balle_rect.left <= AppConfig.mur_epaisseur:
            # Mur à gauche 
            contact_face = "right"
        elif balle_rect.right >= AppConfig.surface_image_fond.get_width() - AppConfig.mur_epaisseur:
            # Mur à droite
            contact_face = "left"
        elif balle_rect.top <= AppConfig.mur_epaisseur:
            # Mur top
            contact_face = "bottom"
        elif balle_rect.top >= AppConfig.surface_image_fond.get_height() - self._balle_hauteur - self._raquette_hauteur \
            and balle_rect.top <= AppConfig.surface_image_fond.get_height() - self._balle_hauteur -self._raquette_hauteur + 1 \
            and balle_rect.left + self._balle_largeur // 2 >= self._raquette_x \
            and balle_rect.left + self._balle_largeur // 2 <= self._raquette_x + self._raquette_largeur:
            # Raquette
            contact_face = "top"
        else:
            for gi in self._grille:
                if gi.kia: continue # Élément dédruit
                if not balle_rect.colliderect( gi.rect ): continue # Pas de contact
                # Contact possible → on teste plus finement, et on détermine la face de contact
                print(f"Contact ? balle_rect: {balle_rect} et gi.rect = {gi.rect}")
                print(f"Position antérieure : ({self._balle_x_origine}, {self._balle_y_origine})")
                balle_rayon:float = balle_rect.width / 2
                balle_centre_x:int = balle_rect.left + (balle_rect.width // 2)
                balle_centre_y:int = balle_rect.top + (balle_rect.height // 2)
                print(f"balle_rayon: {balle_rayon}, balle_centre_x: {balle_centre_x}, balle_centre_y: {balle_centre_y}")
                faces = {
                    'bottom': [(x, gi.y + gi.rect.height) for x in range(gi.x, gi.x + gi.rect.width)],
                    'top': [(x, gi.y) for x in range(gi.x, gi.x + gi.rect.width)],
                    'left': [(gi.x, y) for y in range(gi.y, gi.y + gi.rect.height)],
                    'right': [(gi.x + gi.rect.width, y) for y in range(gi.y, gi.y + gi.rect.height)]
                }
                for face, points in faces.items():
                    for p in points:
                        dx, dy = p[0] - balle_centre_x, p[1] - balle_centre_y
                        distance = math.sqrt(dx**2 + dy**2)
                        if distance <= balle_rayon:
                            contact_face = face
                            break
                    if contact_face is not None: 
                        # brique supprimée ou dégradée selon la dureté et le nombre d'impacts
                        gi.impact += 1
                        gi.kia = gi.element.durete <= gi.impact
                        if gi.kia:  # Remettre le fond
                            self._restaurer_fond(gi.rect.left, gi.rect.top, gi.rect.width, gi.rect.height)
                            s = pygame.mixer.Sound(AppConfig.nom_fichier_son_destruction)
                            s.set_volume(0.3)
                            s.play()
                        else:       # Nouvelle image brique
                            self._surface_ecran.blit(gi.element.surfaces[gi.impact], (gi.rect.left, gi.rect.top))
                        pygame.display.update((gi.rect.left, gi.rect.top, gi.rect.width, gi.rect.height))
                        break
                    
        if contact_face is None: return
        pygame.mixer.Sound(AppConfig.nom_fichier_son_contact).play()
        
        print(f"Contact → {contact_face}")
        print(f"Angle avant → {self._balle_mouvement_angle}")
        # Changement d'angle
        if contact_face == "top":
            self._balle_mouvement_angle = 180 - (self._balle_mouvement_angle - 180)
        if contact_face  == "left":
            if self._balle_mouvement_angle >= 180: 
                # Descendant
                self._balle_mouvement_angle = 180 + (360 - self._balle_mouvement_angle)
            else: 
                # Montant
                self._balle_mouvement_angle = 180 - self._balle_mouvement_angle
        if contact_face  == "bottom":
            self._balle_mouvement_angle = 180 + (180 - self._balle_mouvement_angle)
        if contact_face  == "right":
            if self._balle_mouvement_angle >= 180: 
                # Descendant
                self._balle_mouvement_angle = 360 - (self._balle_mouvement_angle - 180)
            else: 
                # Montant
                self._balle_mouvement_angle = 180 - self._balle_mouvement_angle
        print(f"Angle après → {self._balle_mouvement_angle}")
        if self._balle_mouvement_angle < 0 or self._balle_mouvement_angle > 360: raise Exception("Angle KO")
        print(f"self._balle_mouvement_x_y avant → {self._balle_mouvement_x_y}")
        self._balle_mouvement_x_y = self._get_mouvement_x_y()
        print(f"self._balle_mouvement_x_y après → {self._balle_mouvement_x_y}")
        print('*' * 10)
            
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
            self.deplacer_balle((nouveau_x - self._raquette_x, 0))
        # Récupération du fond pour écraser l'actuelle zone occupée par la raquette
        self._restaurer_fond(self._raquette_x, self._raquette_y, self._raquette_largeur, self._raquette_hauteur)
        # Nouvelle position de la raquette et affichage
        self._raquette_x = nouveau_x
        self._surface_ecran.blit( self._raquette.surfaces[0], (self._raquette_x, self._raquette_y))
        pygame.display.update((self._raquette_x, self._raquette_y,self._raquette_largeur, self._raquette_hauteur))
        
    def _restaurer_fond(self, x:float, y:float, largeur:int, hauteur:int):
        # Conversion / position pixels
        x,y = int(x), int(y)
        # Restauration
        rect_arriere_plan = pygame.Rect(x, y, largeur, hauteur)
        surf_arriere_plan = self._surface_fond.subsurface(rect_arriere_plan)
        self._surface_ecran.blit(surf_arriere_plan, (x, y))
        pygame.display.update((x, y, largeur, hauteur))

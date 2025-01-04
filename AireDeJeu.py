"""
Niveau (plateau de jeu)
"""
import math
import random

import pygame

import AppConfig
from Grille import Grille
from Log import Log

class AireDeJeu:
   
    def __init__(self, nom_fichier_contenu_aire:str):
        """Initialisation"""
        self.balle_lancee = False
        self.raquette_deplacement_gauche = False
        self.raquette_deplacement_droite = False
        """Grille"""
        # Contenu initial de l'aire = éléments = mur et briques
        self._nom_fichier_contenu_aire:str = nom_fichier_contenu_aire
        self._grille:Grille = Grille( self._nom_fichier_contenu_aire )
        """Raquette"""
        self._raquette_x:int = (AppConfig.fond_surface.get_width() - AppConfig.raquette_largeur) // 2
        self._raquette_y:int = AppConfig.fond_surface.get_height() - AppConfig.raquette_hauteur
        """Balle"""
        # Position initiale aléatoire sur la raquette (décalage par rapport au centre de la raquette, à gauche ou à droite, aléatoirement)
        # Décalage de 1/8 de la largeur de la raquete auquel on ajoute aléatoirement jusqu'à 1/4 de la largeur de la raquette
        balle_delta_x:int = ( AppConfig.raquette_largeur // 8 ) + random.randint(0, AppConfig.raquette_largeur) // 6
        if random.randint(0,100) < 50: balle_delta_x = -1 * balle_delta_x
        self._balle_x:float = self._raquette_x + ( AppConfig.raquette_largeur // 2 ) + balle_delta_x
        self._balle_y:float = self._raquette_y - AppConfig.balle_surface.get_height() - 1
        self._balle_mouvement_angle:float = \
            self._get_angle_depuis_adjacent(balle_delta_x) if balle_delta_x >=0 else 90.0 + self._get_angle_depuis_oppose(-1 * balle_delta_x)
        self._balle_mouvement_x_y = self._get_mouvement_x_y()
        
    def _get_angle_depuis_adjacent(self, adja:float, hypo:float|None=None)->float:
        """Retourne un angle en degrés à partir de la longueur de l'hypoténuse et de la longueur du coté adjacent"""
        if hypo is None: hypo = 0.5 * AppConfig.raquette_largeur
        return math.acos(adja/hypo) * 180 / math.pi

    def _get_angle_depuis_oppose(self, oppo:float, hypo:float|None=None)->float:
        """Retourne un angle en degrés à partir de la longueur de l'hypoténuse et de la longueur du coté adjacent"""
        if hypo is None: hypo = 0.5 * AppConfig.raquette_largeur
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
        AppConfig.jeu_surface.blit(AppConfig.fond_surface, (0, 0))
        # Mur (briques du mur)
        for x in range(0, AppConfig.fond_surface.get_width() // AppConfig.mur_epaisseur):
            AppConfig.jeu_surface.blit(AppConfig.mur_surface, (x*AppConfig.mur_epaisseur, 0))
        for y in range(0, AppConfig.fond_surface.get_height() // AppConfig.mur_epaisseur):
            AppConfig.jeu_surface.blit(AppConfig.mur_surface, (0, y*AppConfig.mur_epaisseur))
            AppConfig.jeu_surface.blit(AppConfig.mur_surface, (x*AppConfig.mur_epaisseur, y*AppConfig.mur_epaisseur))
        # Éléménts du décor (briques à casser)
        for item in self._grille:
            sf = AppConfig.elements.get_surface(item.element.identifiant)
            AppConfig.jeu_surface.blit(sf, (item.x, item.y))
        pygame.display.flip()
        # Raquette
        AppConfig.jeu_surface.blit( AppConfig.raquette_surface, (self._raquette_x, self._raquette_y))
        # Balle
        AppConfig.jeu_surface.blit( AppConfig.balle_surface, (self._balle_x, self._balle_y))
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
            self._restaurer_fond(self._balle_x, self._balle_y, AppConfig.balle_largeur, AppConfig.balle_hauteur)
            # Afficher à la nouvelle position
            AppConfig.jeu_surface.blit( AppConfig.balle_surface, (int(nouveau_x), int(nouveau_y)))
            pygame.display.update((int(nouveau_x), int(nouveau_y),AppConfig.balle_largeur, AppConfig.balle_hauteur))

        # Nouvelle position
        self._balle_x = min(AppConfig.balle_x_max, max(AppConfig.balle_x_min,nouveau_x))
        self._balle_y = min(AppConfig.balle_y_max, max(AppConfig.balle_y_min,nouveau_y))

        balle_perdue:bool = False
        if self._balle_y >= AppConfig.balle_y_max:
            balle_perdue |= (self._balle_x + AppConfig.balle_largeur // 2) < self._raquette_x
            balle_perdue |= (self._balle_x + AppConfig.balle_largeur // 2) > self._raquette_x + AppConfig.raquette_largeur
        if balle_perdue: 
            pygame.mixer.Sound(AppConfig.nom_fichier_son_balle_perdue).play()
            pygame.time.delay(3_000)
            raise Exception("Balle perdue!")
            
        """Contact ?"""
        contact_face:str = None
        contact_raquette:bool = False
        
        balle_rect = pygame.Rect(int(self._balle_x), int(self._balle_y), AppConfig.balle_largeur, AppConfig.balle_hauteur)
        
        # Mur à gauche ?
        if balle_rect.left <= AppConfig.mur_epaisseur:
            contact_face = "right"
        # Mur à droite ?
        elif balle_rect.right >= AppConfig.fond_surface.get_width() - AppConfig.mur_epaisseur:
            contact_face = "left"
        # Mur top ?
        elif balle_rect.top <= AppConfig.mur_epaisseur:
            contact_face = "bottom"
        # Raquette ?
        elif balle_rect.top >= AppConfig.fond_surface.get_height() - AppConfig.balle_hauteur - AppConfig.raquette_hauteur \
            and balle_rect.top <= AppConfig.fond_surface.get_height() - AppConfig.balle_hauteur -AppConfig.raquette_hauteur + 1 \
            and balle_rect.left + AppConfig.balle_largeur // 2 >= self._raquette_x \
            and balle_rect.left + AppConfig.balle_largeur // 2 <= self._raquette_x + AppConfig.raquette_largeur:
            contact_face = "top"
            contact_raquette = True
        # Brique ?
        else:
            for gi in self._grille:
                if gi.kia: continue # Élément dédruit
                if not balle_rect.colliderect( gi.rect ): continue # Pas de contact
                # Contact possible → on teste plus finement, et on détermine la face de contact
                balle_rayon:float = balle_rect.width / 2
                balle_centre_x:int = balle_rect.left + (balle_rect.width // 2)
                balle_centre_y:int = balle_rect.top + (balle_rect.height // 2)
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
                            AppConfig.jeu_surface.blit(gi.element.surfaces[gi.impact], (gi.rect.left, gi.rect.top))
                        pygame.display.update((gi.rect.left, gi.rect.top, gi.rect.width, gi.rect.height))
                        break
                    
        if contact_face is None: return
        
        # Son ("musique") au contact
        pygame.mixer.Sound(AppConfig.nom_fichier_son_contact).play()
        
        # Changement d'angle
        if contact_face == "top":
            self._balle_mouvement_angle = 180 - (self._balle_mouvement_angle - 180)
            if contact_raquette:
                if self.raquette_deplacement_droite: self._balle_mouvement_angle -= 20
                if self.raquette_deplacement_gauche: self._balle_mouvement_angle += 20
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
                
        if self._balle_mouvement_angle < 0 or self._balle_mouvement_angle > 360: raise Exception("Angle KO")
        
        # "Correction de l'angle si "extrème"
        if self._balle_mouvement_angle == 360 or self._balle_mouvement_angle < AppConfig.balle_angles_autorises[0][0]:
            self._balle_mouvement_angle = AppConfig.balle_angles_autorises[0][0]
        if self._balle_mouvement_angle <= 180 and self._balle_mouvement_angle > AppConfig.balle_angles_autorises[0][1]:
            self._balle_mouvement_angle = AppConfig.balle_angles_autorises[0][1]
        if self._balle_mouvement_angle > 180 and self._balle_mouvement_angle < AppConfig.balle_angles_autorises[1][0]:
            self._balle_mouvement_angle = AppConfig.balle_angles_autorises[1][0]
        if self._balle_mouvement_angle > AppConfig.balle_angles_autorises[1][1]:
            self._balle_mouvement_angle = AppConfig.balle_angles_autorises[1][1]

        self._balle_mouvement_x_y = self._get_mouvement_x_y()
            
    def deplacer_raquette(self, delta_x:int, balle_lancee:bool):
        """Déplacer la raquette et, éventuellement, la balle si pas encore lancée et donc toujours 'posée' sur la raquette"""
        if delta_x < 0 and self._raquette_x <= AppConfig.raquette_x_min: return # ignoré (déjà bord gauche)
        if delta_x > 0 and self._raquette_x >= AppConfig.raquette_x_max: return # ignoré (déjà bord droite)
        
        nouveau_x = self._raquette_x + delta_x
        
        nouveau_x = max(AppConfig.raquette_x_min, nouveau_x)
        nouveau_x = min(AppConfig.raquette_x_max, nouveau_x)
        
        if self._raquette_x == nouveau_x: return
        
        # Si la balle est posée sur la raquette, c'est à dire si elle n'a pas été lancée, alors elle doit bouger avec la raquette        
        if not balle_lancee: 
            self.deplacer_balle((nouveau_x - self._raquette_x, 0))
        # Récupération du fond pour écraser l'actuelle zone occupée par la raquette
        self._restaurer_fond(self._raquette_x, self._raquette_y, AppConfig.raquette_largeur, AppConfig.raquette_hauteur)
        # Nouvelle position de la raquette et affichage
        self._raquette_x = nouveau_x
        AppConfig.jeu_surface.blit( AppConfig.raquette_surface, (self._raquette_x, self._raquette_y))
        pygame.display.update((self._raquette_x, self._raquette_y,AppConfig.raquette_largeur, AppConfig.raquette_hauteur))
        
    def _restaurer_fond(self, x:float, y:float, largeur:int, hauteur:int):
        # Conversion / position pixels
        x,y = int(x), int(y)
        # Restauration
        rect_arriere_plan = pygame.Rect(x, y, largeur, hauteur)
        surf_arriere_plan = AppConfig.fond_surface.subsurface(rect_arriere_plan)
        AppConfig.jeu_surface.blit(surf_arriere_plan, (x, y))
        pygame.display.update((x, y, largeur, hauteur))

import os
import pygame

import AppConfig
from Grille import Grille
from NiveauPlateau import NiveauPlateau

pygame.init()

# Fenêtre de l'application
pygame.display.set_caption("pyCasseBriques")
ecran = pygame.display.set_mode((1100, 810))

# Image de fond
img_fond = pygame.image.load("img/fond.png").convert_alpha()
ecran.blit(img_fond, (0, 0))

# Charger un niveau (une grille de test)
np = NiveauPlateau(ecran, os.path.join(AppConfig.dossier_csv, "grille_plateau_test.csv"))
np.display()

# C'est parti ! (à ce stade, beaucoup reste à faire ;-))
img_raquete = pygame.image.load("img/raquette.png").convert_alpha()
ecran.blit(img_raquete, (210, 780))

img_balle = pygame.image.load("img/balle.png").convert_alpha()
ecran.blit(img_balle, (300, 720))

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
    
pygame.quit()

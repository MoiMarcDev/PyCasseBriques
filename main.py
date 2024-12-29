import os
import pygame

import AppConfig
from AireDeJeu import AireDeJeu

pygame.init()

# Fenêtre de l'application
pygame.display.set_caption("pyCasseBriques")
ecran = pygame.display.set_mode((1100, 810))

# Image de fond
img_fond = pygame.image.load("img/fond.png").convert_alpha()
ecran.blit(img_fond, (0, 0))

# Charger un niveau (une grille de test)
jeu = AireDeJeu(ecran, os.path.join(AppConfig.dossier_csv, "grille_plateau_vide.csv"))
jeu.display()

# C'est parti ! (à ce stade, beaucoup reste à faire ;-))
#img_balle = pygame.image.load("img/balle.png").convert_alpha()
#ecran.blit(img_balle, (300, 720))

running = True

raquette_gauche, raquette_droite = False, False

while running:
    for event in pygame.event.get():
        # Quitter le jeu
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        # Déplacer la raquette vers la gauche
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: raquette_gauche = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT: raquette_gauche = False
        # Déplacer la raquette vers la droite
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: raquette_droite = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT: raquette_droite = False

    if raquette_gauche: jeu.deplacer_raquette(-1)
    if raquette_droite: jeu.deplacer_raquette(+1)

    # Mettre à jour toute la surface d'affichage pour refléter les modifications apportées à l'écran
    pygame.display.flip()
    
    pygame.time.delay(2)
    
pygame.quit()

import os
import pygame

import AppConfig
from AireDeJeu import AireDeJeu

pygame.init()

# Fenêtre de l'application
pygame.display.set_caption("pyCasseBriques")
ecran = pygame.display.set_mode((1100, 810))

# Charger un niveau (une grille de test)
jeu = AireDeJeu(ecran, os.path.join(AppConfig.nom_dossier_csv, "grille_plateau_vide.csv"))
jeu.afficher()

continuer = True

raquette_gauche, raquette_droite = False, False

while continuer:
    for e in pygame.event.get():
        # Quitter le jeu
        if e.type == pygame.QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
            continuer = False
        # Déplacer la raquette vers la gauche
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT: raquette_gauche = True
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT: raquette_gauche = False
        # Déplacer la raquette vers la droite
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT: raquette_droite = True
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT: raquette_droite = False

    if raquette_gauche: jeu.deplacer_raquette(-1)
    if raquette_droite: jeu.deplacer_raquette(+1)

    # Mettre à jour toute la surface d'affichage pour refléter les modifications apportées à l'écran
    pygame.display.flip()
    
    pygame.time.delay(1)
    
pygame.quit()

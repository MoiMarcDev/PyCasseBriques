import os
import pygame

import AppConfig
from AireDeJeu import AireDeJeu

pygame.init()

# Fenêtre de l'application
pygame.display.set_caption("pyCasseBriques")
ecran = pygame.display.set_mode((1100, 810))

# Charger un niveau (une grille de test)
aire_de_jeu = AireDeJeu(ecran, os.path.join(AppConfig.nom_dossier_csv, "grille_plateau_vide.csv"))
aire_de_jeu.afficher()

continuer, balle_lancee = True, False

evenement, raquette_gauche, raquette_droite = False, False, False

while continuer:
    for e in pygame.event.get():
        evenement = True
        # Quitter le jeu
        if e.type == pygame.QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
            continuer = False
        # Déplacer la raquette vers la gauche
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT: raquette_gauche = True
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT: raquette_gauche = False
        # Déplacer la raquette vers la droite
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT: raquette_droite = True
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT: raquette_droite = False

    if raquette_gauche: aire_de_jeu.deplacer_raquette(-1, balle_lancee)
    if raquette_droite: aire_de_jeu.deplacer_raquette(+1, balle_lancee)

    pygame.time.delay(1)
    
pygame.quit()

import os
import pygame

import AppConfig
from AireDeJeu import AireDeJeu
from Log import Log

pygame.init()

Log.set_callback(print)

# Fenêtre de l'application
pygame.display.set_caption(AppConfig.fenetre_titre)

# Mixer (sons)
pygame.mixer.init()
pygame.mixer.Sound(AppConfig.nom_fichier_son_debut_jeu).play()

# Charger une aire de jeu (=les éléments (briques) du niveau (platea))
aire_de_jeu = AireDeJeu(os.path.join(AppConfig.nom_dossier_csv, "grille_plateau_test.csv"))
aire_de_jeu.afficher()

quitter_jeu = False
while not quitter_jeu:
    for e in pygame.event.get():
        # Quitter le jeu
        if e.type == pygame.QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
            quitter_jeu = True
            break
        # Déplacer la raquette vers la gauche
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT: aire_de_jeu.raquette_deplacement_gauche = True
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT: aire_de_jeu.raquette_deplacement_gauche = False
        # Déplacer la raquette vers la droite
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT: aire_de_jeu.raquette_deplacement_droite = True
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT: aire_de_jeu.raquette_deplacement_droite = False
        # Barre d'espace
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and not aire_de_jeu.balle_lancee:
            aire_de_jeu.balle_lancee = True

    if aire_de_jeu.raquette_deplacement_gauche: aire_de_jeu.deplacer_raquette(-1, aire_de_jeu.balle_lancee)
    if aire_de_jeu.raquette_deplacement_droite: aire_de_jeu.deplacer_raquette(+1, aire_de_jeu.balle_lancee)
    if aire_de_jeu.balle_lancee: aire_de_jeu.deplacer_balle()

    pygame.time.delay(AppConfig.jeu_delai_pause_ms)
    
pygame.quit()

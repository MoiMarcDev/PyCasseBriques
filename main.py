import pygame

from Niveau import Niveau

pygame.init()

pygame.display.set_caption("pyCasseBriques")
ecran = pygame.display.set_mode((1100, 810))

continuer = True

img_fond = pygame.image.load("img/fond.png").convert_alpha()
ecran.blit(img_fond, (0, 0))

img_mur = pygame.image.load("img/mur.png").convert_alpha()
for x in range(0,27):
    ecran.blit(img_mur, (30 * x, 0))
for x in range(0,27):
    ecran.blit(img_mur, (0, 30 * x))
    ecran.blit(img_mur, (810, 30 * x))

img_raquete = pygame.image.load("img/raquette.png").convert_alpha()
ecran.blit(img_raquete, (210, 780))

img_balle = pygame.image.load("img/balle.png").convert_alpha()
ecran.blit(img_balle, (300, 720))

y_brique, nb_brique = (450, 12)
briques = ["bleu_fonce", "gris_fonce", "marron_fonce", "vert_fonce", "orange", "violet", "jaune", "rouge", "bleu_clair", "gris_clair", "marron_clair", "vert_clair"]
for b in briques:
    img_brique = pygame.image.load("img/brique_" + b + ".png").convert_alpha()
    for x in range(nb_brique):
        ecran.blit(img_brique, (30 + (60 * x), y_brique))
    nb_brique -= 1
    y_brique -= 30

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
    
pygame.quit()

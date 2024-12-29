### Aire de jeu, Tableau d'affichage, Pixels, Fichier CSV
On divise la surface de l'application en deux zones:
- à gauche, l'aire de jeu (en gros, le mur à casser avec ses briques, la raquette, et la balle)
- à droite, le tableau d'affichage (niveau, score, temps restant, nombre de balles, nombre de raquettes)

Pour chaque zone, on travaillera au niveau du pixel, notamment pour gérer les collisions dans l'aire de jeu.

L'aire de jeu a une dimension de 840 x 810 pixels (largeur x hauteur) dans laquelle on positionne les éléments qui forment le "décor" (_grille de départ_) de chaque niveau :
- Un élément == un mur ou une brique
- Un mur a une dimension de (30x30), une brique une dimension de (60x30) ← contraintes pour cette version du jeu
- Chaque élément occupe  une zone rectangulaire (ou carré) et possède des coordonnées qui correspondent à la localisation, dans la grille, du coin haut et gauche de l'élément
- Chaque élément a une dureté qui vaut 0 à 3 ; typiquement :
    - 0 : incassable (ex: mur)
    - 1 : se brise au premier contact avec la balle (ex: brique)
    - 2 : résiste à un premier impact, et se brise au second impact avec la balle
    - 3 : nécessite 3 impacts avant de casser

Dans le sous-dossier "csv/", on stockera :
- un fichier "element.csv" avec les informations sur les différents éléments qui peuvent etre positionés sur une grille
- des fichiers "grille_niveau_x.csv" où x représente le numéro du niveau (du plateau) avec les différents éléments et leurs positions

La structure de "element.csv" est :

| Identifiant         | Durete | Image                   | Image_impact_1            | Image_impact_2            |
|---------------------|--------|-------------------------|---------------------------|---------------------------|
| MUR                 | 0      | mur.png                 |                           |                           |
| RAQUETTE_GRANDE     | 0      | raquette_grande.png     |                           |                           |
| RAQUETTE            | 0      | raquette.png            |                           |                           |
| RAQUETTE_PETITE     | 0      | raquette_petite.png     |                           |                           |
| BRIQUE_BLEU_FONCE   | 3      | brique_bleu_fonce.png   | brique_bleu_fonce_1.png   | brique_bleu_fonce_2.png   |
| BRIQUE_GRIS_FONCE   | 3      | brique_gris_fonce.png   | brique_gris_fonce_1.png   | brique_gris_fonce_2.png   |
| BRIQUE_MARRON_FONCE | 3      | brique_marron_fonce.png | brique_marron_fonce_1.png | brique_marron_fonce_2.png |
| BRIQUE_VERT_FONCE   | 3      | brique_vert_fonce.png   | brique_vert_fonce_1.png   | brique_vert_fonce_2.png   |
| BRIQUE_ORANGE       | 2      | brique_orange.png       | brique_orange_1.png       |                           |
| BRIQUE_ROUGE        | 2      | brique_rouge.png        | brique_rouge_1.png        |                           |
| BRIQUE_VIOLET       | 2      | brique_violet.png       | brique_violet_1.png       |                           |
| BRIQUE_BLEU         | 1      | brique_bleu.png         |                           |                           |
| BRIQUE_JAUNE        | 1      | brique_jaune.png        |                           |                           |
| BRIQUE_VERT         | 1      | brique_vert.png         |                           |                           |

Ci-dessous la structure de d'un fichier "grille_niveau_x.csv", avec un exemple d'un possible contenu :

|   X |   Y | Element             |
|-----|-----|---------------------|
|   0 |   0 | MUR                 |
|   0 |  30 | MUR                 |
|  .. |  .. | ..                  |
|   0 | 780 | MUR                 |
| 710 |   0 | MUR                 |
| 870 |  30 | MUR                 |
|  .. |  .. | ..                  |
| 710 | 780 | MUR                 |
|  30 |   0 | MUR                 |
|  60 |   0 | MUR                 |
|  .. |  .. | ..                  |
| 780 |   0 | MUR                 |
|  30 | 600 | BRIQUE_MARRON_FONCE |
|  90 | 600 | BRIQUE_MARRON_FONCE |
| 150 | 600 | BRIQUE_MARRON_FONCE |
|  .. |  .. | ..                  |

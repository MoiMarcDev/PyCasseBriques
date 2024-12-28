### Pixels, Niveau & Grille, fichier CSV
On travaillera au niveau du pixel, notamment pour gérer les collisions.

Toutefois, à un niveau plus "macro" on représentera chaque niveau de jeu sous la forme d'une grille :
- La surface de jeu a une dimension de 840 x 810 pixels (largeur x hauteur)
- Chaque case a une dimension de 30x30 pixles
- La grille a une largeur de 28 "cases" et une hauteur de 27 "cases" (soit 756 cases au total)

Dans cette grille, on positionne les éléments qui forment le "décor" de chaque niveau :
- Un élément == un mur ou une brique
- Chaque élément possède une dimension (=nombre de cases) pour sa largeur et pour sa hauteur (largeur x hauteur)
- Un mur a une dimension de (1x1), une brique une dimension de (2x1) ; en fait la hauteur est toujours de 1; seule la largeur peut varier
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

| Identifiant         | Durete | Largeur | Image                   | Image_impact_1            | Image_impact_2            |
|---------------------|--------|---------|-------------------------|---------------------------|---------------------------|
| MUR                 | 0      | 1       | mur.png                 |                           |                           |
| BRIQUE_BLEU_FONCE   | 3      | 2       | brique_bleu_fonce.png   | brique_bleu_fonce_1.png   | brique_bleu_fonce_2.png   |
| BRIQUE_GRIS_FONCE   | 3      | 2       | brique_gris_fonce.png   | brique_gris_fonce_1.png   | brique_gris_fonce_2.png   |
| BRIQUE_MARRON_FONCE | 3      | 2       | brique_marron_fonce.png | brique_marron_fonce_1.png | brique_marron_fonce_2.png |
| BRIQUE_VERT_FONCE   | 3      | 2       | brique_vert_fonce.png   | brique_vert_fonce_1.png   | brique_vert_fonce_2.png   |
| BRIQUE_ORANGE       | 2      | 2       | brique_orange.png       | brique_orange_1.png       |                           |
| BRIQUE_ROUGE        | 2      | 2       | brique_rouge.png        | brique_rouge_1.png        |                           |
| BRIQUE_VIOLET       | 2      | 2       | brique_violet.png       | brique_violet_1.png       |                           |
| BRIQUE_BLEU         | 1      | 2       | brique_bleu.png         |                           |                           |
| BRIQUE_JAUNE        | 1      | 2       | brique_jaune.png        |                           |                           |
| BRIQUE_VERT         | 1      | 2       | brique_vert.png         |                           |                           |

Ci-dessous la structure de d'un fichier "grille_niveau_x.csv", avec un exemple d'un possible contenu :

|  X |  Y | Element             |
|----|----|---------------------|
|  0 |  0 | MUR                 |
|  0 |  1 | MUR                 |
| .. | .. | ..                  |
|  0 | 26 | MUR                 |
| 27 |  0 | MUR                 |
| 27 |  1 | MUR                 |
| .. | .. | ..                  |
| 27 | 26 | MUR                 |
|  1 |  0 | MUR                 |
|  2 |  0 | MUR                 |
| .. | .. | ..                  |
| 26 |  0 | MUR                 |
|  1 | 20 | BRIQUE_MARRON_FONCE |
|  3 | 20 | BRIQUE_MARRON_FONCE |
|  5 | 20 | BRIQUE_MARRON_FONCE |
| .. | .. | ..                  |

# pyCasseBriques

Petit jeu de casse-briques en Python avec la librairie Pygame

Le projet consiste à développer un jeu casse-briques en 2D en utilisant la bibliothèque Pygame de Python. 
Le joueur contrôle une raquette pour faire rebondir une balle et détruire des briques. 
Le joueur doit détruire toutes les briques sur l'écran pour passer au niveau suivant.

### Fonctionnalités
- Raquette Contrôlable : Le joueur pourra déplacer une raquette horizontalement avec les touches du clavier pour renvoyer la balle.
- Balle Rebondissante : La balle rebondira sur les murs, la raquette et les briques.
- Briques : Les briques se casseront lorsqu'elles seront touchées par la balle.
- Niveaux Multiples : Le jeu comportera plusieurs niveaux avec des configurations de briques différentes.
- Score : Un système de score qui augmentera à chaque brique détruite.

### Technologies Utilisées :
- Python: Le langage principal utilisé pour le développement du jeu.
- Pygame: Une bibliothèque Python pour le développement de jeux 2D avec gestion des graphismes, des événements et des interactions.

### Étapes de développement (plan initial):
- Installation et Configuration de Pygame : Installer Pygame et configurer l'environnement de développement.
- Création de la Fenêtre de Jeu : Configurer la fenêtre de jeu et afficher un arrière-plan de base.
- Développement de la Raquette : Programmer les contrôles de la raquette pour la déplacer horizontalement.
- Mouvement de la Balle : Implémenter la logique pour faire rebondir la balle sur les murs, la raquette et les briques.
- Création des Briques : Ajouter des briques destructibles à l'écran.
- Gestion des Collisions : Développer la logique pour gérer les collisions entre la balle et les briques.
- Système de Niveaux : Concevoir plusieurs niveaux avec des configurations de briques différentes.

### Notes

#### Aire de jeu, Tableau d'affichage, Pixels, Fichier CSV
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

#### Environement 
- python -m venv env

#### Raccoucis
- ctrl-k v → affiche preview du document markdown
- ctrl j → agrandir ou minimiser le terminal

#### Ajout de Git Bash à Visual Studio Code
- lien : https://www.geeksforgeeks.org/how-to-integrate-git-bash-with-visual-studio-code/
- File->Preferences->Settings
- click on the Open Settings(JSON) (en haut à droite)
- add the below properties at the last of all settings :
> "terminal.integrated.profiles.windows":{"Git Bash":{"path":"C:\\Program Files\\Git\\bin\\bash.exe"},  },
"terminal.integrated.defaultProfile.windows": "Git Bash"

- reopen VS Code then you will see that Git Bash has been integrated

#### Modification du "prompt" Git Bash
- faire une copie de sauvegarde du fichier C:\Program Files\Git\etc\profile.d\git-prompt.sh
- ouvrir ce fichier en tant qu'administrateur (dans Notepad par exemple)
- remplacer :
> 	PS1="$PS1"'\[\033[32m\]'       # change to green
	PS1="$PS1"'\u@\h '             # user@host<space>
	PS1="$PS1"'\[\033[35m\]'       # change to purple
	PS1="$PS1"'$MSYSTEM '          # show MSYSTEM
	PS1="$PS1"'\[\033[33m\]'       # change to brownish yellow
	PS1="$PS1"'\w'                 # current working directory

Par :
>   PS1="$PS1"'`pwd`'   	       # Dossier courant réel !

### playsound
- /!\ petite difficulté à l'installation de la librairie playsound:
    - était ko (=produisait une erreur): 
	    > pip install playsound
		> python -m pip install playsound
		- *erreur* : "subprocess-exited-with-error × Getting requirements to build wheel did not run successfully"
		- erreur toujours présente après :
		>"pip install --upgrade wheel"
    - *Ok* en installant directement depuis le repository git 
	> pip install git+https://github.com/taconi/playsound.git
	- finalement, utilisation de pygame.mixer.Sound en standard avec pygame ;-)

#### Matériels
- Graphisme : 
    - https://opengameart.org/content/breakout-brick-breaker-tile-set-free
    - https://opengameart.org/content/breakout-set
	- Images éventuellement retravaillées avec GIMP
- Sons :
    - https://mixkit.co/free-sound-effects/game/
	- https://pixabay.com/sound-effects/ 
	- Conversion (changement de format) si besoin → avec VLC

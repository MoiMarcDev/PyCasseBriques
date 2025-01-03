import csv

import pygame

import AppConfig
from Element import ElementItem

"""Grille de jeu"""

class GrilleItem:
    def __init__(self, x: int, y: int, elt:ElementItem):
        self.x:int = x
        self.y:int = y
        self.element:ElementItem = elt
        self.rect:pygame.Rect = pygame.Rect(x, y, elt.largeur, elt.hauteur)
        self.impact:int = 0
        self.kia:bool = False
        
    def __repr__(self):
        return f"{type(self)} → x={self.x}; y={self.y}; elt={self.element}"

class Grille:
    def __init__(self, nom_fichier_csv:str):
        self._nom_fichier_csv:str = nom_fichier_csv
        
        self._elements:list[GrilleItem] = []
        with open(self._nom_fichier_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self._elements.append(
                        GrilleItem(
                            int(row['x']), 
                            int(row['y']), 
                            AppConfig.elements.get_element(row['identifiant']) 
                        )
                )
        
    def __iter__(self):
        """Fournir un itérateur"""
        for x in self._elements:
            yield x

#############################

if __name__ == "__main__":
    import os
    import AppConfig
    g = Grille( os.path.join(AppConfig.nom_dossier_csv, "grille_plateau_test.csv") )
    for e in g:
        print(e)
